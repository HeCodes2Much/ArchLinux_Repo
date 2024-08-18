#!/usr/bin/env bash

# Repo update script using repo-add, rsync, and git
# written by linuxrepos for archlinux.repo.063240.xyz.

readonly RPATH="$(cd "$(dirname "$0")" || exit ; pwd -P)"
readonly ARCHDIR="$(basename "$RPATH")"
readonly REPO_PATH="$(sed "s~/${ARCHDIR}~~" <<< "$RPATH")"
readonly TYPE=$1

if ! hash git &>/dev/null; then
    echo "ERROR: Script requires both rsync and git installed"
    exit 1
fi

commit_repo() {
    cd "$REPO_PATH/$ARCHDIR" || return
    rm -f linuxrepos.*
    repo-add --verify --sign linuxrepos.db.tar.gz ./*.pkg.tar.zst
    rm -f linuxrepos.db linuxrepos.db.sig
    cp -f linuxrepos.db.tar.gz linuxrepos.db
    cp -f linuxrepos.db.tar.gz.sig linuxrepos.db.sig
    rm -f linuxrepos.files linuxrepos.files.sig
    cp -f linuxrepos.files.tar.gz linuxrepos.files
    cp -f linuxrepos.files.tar.gz.sig linuxrepos.files.sig
}

commit_git() {
    if [[ -e $HOME/.gitconfig ]]; then
        cd "$REPO_PATH" || return
        git add .
        git commit -S -m "Repo update $(date +%d/%m/%Y_%H:%M:%S_%Z)"
        git push origin main
    else
        echo
        echo "ERROR: You must setup git to use this"
        exit 1
    fi
}

if [[ -d $REPO_PATH/$ARCHDIR ]]; then
    commit_repo
    if [[ -n "$TYPE" ]]; then
        if [[ "$TYPE" == "--push" ]]; then
            echo -e "\nPushing to git origin"
            commit_git
        fi
    fi
else
    echo -e "\nCannot find repo directory: '$REPO_PATH/$ARCHDIR'"
    exit 1
fi

if [[ -n "$TYPE" ]]; then
    if [[ "$TYPE" == "--push" ]]; then
        echo "################################################################"
        echo "###################    Git Push Done      ######################"
        echo "################################################################"
    fi
fi
exit 0
