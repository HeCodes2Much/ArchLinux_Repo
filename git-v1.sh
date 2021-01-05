#!/usr/bin/env bash
##################################################################################################################
# Author 	: 	TheCynicalLiger
# Website	:	https://github.com/TheCynicalLiger/
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################
readonly TYPE=$1

# checking if I have the latest files from github
echo "Checking for newer files online first"
git pull

# Below command will backup everything inside the project folder
if [[ -n "$TYPE" ]]; then
    if [[ "$TYPE" == "--push" ]]; then
        ./x86_64/updaterepo.sh $TYPE
    else
        ./x86_64/updaterepo.sh
    fi
else
    ./x86_64/updaterepo.sh
fi

git send-email --subject-prefix="${PWD##*/}][PATCH" --to wayne6324@gmail.com -1
