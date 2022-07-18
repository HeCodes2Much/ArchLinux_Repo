import glob
import subprocess
import time
import os
import re
import urllib.request
import platform
import json
import math
import shutil
from datetime import datetime as dt

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{d}', str(t.day) + suffix(t.day))

datetime = custom_strftime('%a {d}, %b %Y at %I:%M:%S%p', dt.now())

def filebrowser(ext=""):
    "Returns files with an extension"
    return [file for file in glob.glob(f"*{ext}")]

files = filebrowser(".pkg.tar.zst")

files.sort()

pkgcount = 0
for file in files:
    pkgcount += 1
print(f"There are {pkgcount} packages to be uploaded!\n")

home = os.path.expanduser("~")
readme = open('../README.md','w')
installme = open(home + '/.config/package-list','w')
data = []
readme.write(f"# <img src='favicon.svg' width='64' height='64'> The Repo Club's Arch Repo <img src='favicon.svg' width='64' height='64'>\n")
badges = f"\n<p align='center'>\n\
  <img src='https://img.shields.io/badge/Maintained-Yes-green?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/last-commit/The-Repo-Club/Arch.TheRepo.Club?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/repo-size/The-Repo-Club/Arch.TheRepo.Club?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/static/v1?label=Packages&message={pkgcount}&colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/license/The-Repo-Club/Arch.TheRepo.Club?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/issues/The-Repo-Club/Arch.TheRepo.Club?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/stars/The-Repo-Club/Arch.TheRepo.Club?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/forks/The-Repo-Club/Arch.TheRepo.Club?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/commit-activity/m/The-Repo-Club/Arch.TheRepo.Club?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
</p>\n"
readme.write(badges)
readme.write(f"\n## Software\n")

def get_file_name(file):
    head = "head -n5"
    awk = "awk '{$1=$2=\"\"; print $0}'"
    command = f"bsdtar -xOf {file} .BUILDINFO | {head} | grep -I pkgname | {awk} | sed -n 1p"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    return str(output[0].decode()).strip()

def get_file_version(file):
    head = "head -n5"
    awk = "awk '{$1=$2=\"\"; print $0}'"
    command = f"bsdtar -xOf {file} .BUILDINFO | {head} | grep -I pkgver | {awk} | sed -n 1p"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    return str(output[0].decode()).strip()

def get_file_date(file):
    file_date = os.path.getmtime(file)
    return str(time.strftime('%H:%M:%S %d-%m-%Y', time.localtime(file_date)))

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return str("%s %s" % (s, size_name[i]))

def get_file_size(filename):
    st = os.stat(filename)
    return str(convert_size(st.st_size))

for file in files:
    name = str(get_file_name(file))
    version = str(get_file_version(file))
    size = str(get_file_size(file))
    date = str(get_file_date(file))

    print(f"File Updated: Name ({name}), Version ({version}) Size {size} Date {date}")

    userpac = "<p> <span class='red'>[</span> <span class='yellow'>arch</span><span class='green'>@</span><span class='purple'>therepo.club</span> <span class='red'>~]</span> <br> <span class='green'>pacman</span> <span class='orange'>-Si</span>"
    pacgrep = "<span class='purple'>|</span> <span class='green'>grep</span> <span class='yellow'>'Name\|Version\|Installed\|Build'</span> <span class='purple'>|</span> <span class='green'>awk</span> <span class='orange'>-F</span><span class='yellow'>':' '{print $2}'<span> <span class='purple'>|</span> <span class='green'>sed</span> <span class='yellow'>':a;N;$!ba;s/\\n/ |/g'</span><br>"

    readme.write(f"{userpac} <span class='foreground'><a href='docs/{name}'>{name}</a></span> {pacgrep} <span class='foreground'><a href='docs/{name}'>{name} \t|\t {version} \t|\t {size} \t|\t {date}</a></span> </p>\n")

    installme.write(f"{name}\n")
    data.append(f"{name}")

multiline_addrepo = (f"\n## Add my repo\n"
f"* **Maintainer:** [The-Repo-Club](https://aur.archlinux.org/account/The-Repo-Club/)\n"
f"* **Description:**  A repository with some AUR packages that the team uses\n"
f"* **Upstream page:** https://arch.therepo.club/\n"
f"* **Key-ID:** 75A3 8DC6 84F1 A0B8 0891  8BCE E30E C2FB FB05 C44F \n"
f"* **Fingerprint:** [download](http://pgp.net.nz:11371/pks/lookup?op=vindex&fingerprint=on&search=0xE30EC2FBFB05C44F)\n"
f"\nAppend to */etc/pacman.conf*:\n```\n[therepoclub]\nSigLevel = Required DatabaseOptional\nServer = https://arch.therepo.club/$arch/\n```"
f"\nTo check signature, add my key:\n"
f"```\nsudo pacman-key --keyserver hkp://pgp.net.nz --recv-key BFC53564DA0DD9E5D02D0B409F12B9FF50E52583\nsudo pacman-key --keyserver hkp://pgp.net.nz --lsign-key BFC53564DA0DD9E5D02D0B409F12B9FF50E52583\n```")

readme.write(multiline_addrepo)

multiline_showsupport = (f"\n## Show your support\n"
f"\nGive a ⭐️ if this project helped you!\n"
f"\nThis README was generated with ❤️ by [The-Repo-Club](https://github.com/The-Repo-Club/)\n"
f"*   Last updated on: {datetime}\n")

readme.write(multiline_showsupport)

readme.close()
shutil.copyfile('../README.md', '../repo.md')

json_string = json.dumps(data, indent=4)
with open('../packages.json', 'w') as outfile:
    outfile.write(json_string)

