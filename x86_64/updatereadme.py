import glob
import subprocess
import time
import os
import re
import urllib.request
import json
from datetime import datetime as dt

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{d}', str(t.day) + suffix(t.day))

datetime = custom_strftime('%a {d}, %b %Y at %I:%M:%S%p', dt.now())

home = os.path.expanduser("~")
readme = open('../README.md','w')
installme = open(home + '/.config/package-list','w')
readme.write(f"# <img src='favicon.ico'> The Repo Club's Arch Repo <img src='favicon.ico'>\n")
badges = '\n<p align="center">\n\
  <img src="https://img.shields.io/badge/Maintained-Yes-green?color=red&style=flat-square">\n\
  <img src="https://img.shields.io/github/last-commit/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square">\n\
  <img src="https://img.shields.io/github/repo-size/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square">\n\
  <img src="https://img.shields.io/static/v1?label=License&message=CC%20BY-NC-SA%204.0&color=red&style=flat-square">\n\
  <img src="https://img.shields.io/github/issues/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square">\n\
  <img src="https://img.shields.io/github/stars/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square">\n\
  <img src="https://img.shields.io/github/forks/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square">\n\
  <img src="https://img.shields.io/github/commit-activity/m/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square">\n\
</p>\n'
readme.write(badges)
readme.write(f"\n## Software\n")

def filebrowser(ext=""):
    "Returns files with an extension"
    return [file for file in glob.glob(f"*{ext}")]

files = filebrowser(".pkg.tar.zst")

files.sort()

def get_file_name(file):
    awk1 = "awk '{print $0}'"
    awk2 = "awk '{$1=$2=\"\"; print $0}'"
    command = f"bsdtar -xOf {file} | {awk1} | grep -I pkgname | {awk2}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    name = str(output[0].decode()).strip()

    return name

def get_file_version(file):
    awk1 = "awk '{print $0}'"
    awk2 = "awk '{$1=$2=\"\"; print $0}'"
    command = f"bsdtar -xOf {file} | {awk1} | grep -I pkgver | {awk2}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    version = str(output[0].decode()).strip()

    return version

def get_aur_name(name):
    packages = []
    response = urllib.request.urlopen(f"https://aur.archlinux.org/rpc/?v=5&type=search&arg={name}")
    data = json.loads(response.read())

    title = data["results"]
    for titles in title:
        new_name = titles["Name"]
        packages.append(new_name)
    if f"{name}" in packages:
        return(f"{name}")
    elif f"{name}-git" in packages:
        return(f"{name}-git")
    elif f"{name}-bin" in packages:
        return(f"{name}-bin")
    else:
        return(f"{name}")

pkgcount = 0
for file in files:
    pkgcount += 1
    ignore = open("../ignorepackages", "r").read().splitlines() 
    name = str(get_file_name(file))
    if name not in ignore:
        version = str(get_file_version(file))
        if not name:
            name = str(get_file_name(file))
        if not version:
            version = str(get_file_version(file))

        print(f"File Updated: ({name} v{version})")
        aur_name = get_aur_name(name)

        readme.write(f"*   [{name}](docs/{name}/) Version: {version} ![AUR maintainer](https://img.shields.io/aur/maintainer/{aur_name}?color=blue&style=flat-square) ![AUR maintainer](https://img.shields.io/aur/license/{aur_name}?color=orange&style=flat-square)\n")
        installme.write(f"{name}\n")
print(f"There have been {pkgcount} packages uploaded!\n")

multiline_addrepo = (f"\n## Add my repo\n"
f"* **Maintainer:** [TheCynicalTeam](https://aur.archlinux.org/account/TheCynicalTeam/)\n"
f"* **Description:**  A repository with some AUR packages that the team uses\n"
f"* **Upstream page:** https://arch.therepo.club/\n"
f"* **Key-ID:** 10DF 44AC D4C8 4539 53B7 CCBA 206A DED6 6160 901B\n"
f"* **Fingerprint:** [download](http://pgp.net.nz:11371/pks/lookup?op=vindex&fingerprint=on&search=0x96414492E2220753)\n"
f"\nAppend to */etc/pacman.conf*:\n```\n[therepoclub]\nSigLevel = Required DatabaseOptional\nServer = https://arch.therepo.club/$arch/\n```"
f"\nTo check signature, add my key:\n"
f"```\nsudo pacman-key --keyserver hkp://pgp.net.nz --recv-key 75A38DC684F1A0B808918BCEE30EC2FBFB05C44F\nsudo pacman-key --keyserver hkp://pgp.net.nz --lsign-key 75A38DC684F1A0B808918BCEE30EC2FBFB05C44F\n```")

readme.write(multiline_addrepo)

multiline_showsupport = (f"\n## Show your support\n"
f"\nGive a ⭐️ if this project helped you!\n"
f"\nThis README was generated with ❤️ by [TheCynicalTeam](https://github.com/TheCynicalTeam/)\n"
f"*   Last updated on: {datetime}\n")

readme.write(multiline_showsupport)

readme.close()
