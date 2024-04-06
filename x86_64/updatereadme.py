import glob
import subprocess
import time
import os
import io
import json
import math
import shutil
import zstandard
from datetime import datetime as dt


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(format, t):
    return t.strftime(format).replace("{d}", str(t.day) + suffix(t.day))


datetime = custom_strftime("%a {d}, %b %Y at %I:%M:%S%p", dt.now())


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
readme = open("../README.md", "w")
installme = open(home + "/.config/package-list", "w")
data = []
readme.write(
    f"# <img src='favicon.svg' width='64' height='64'> Arch Linux Repo <img src='favicon.svg' width='64' height='64'>\n"
)
badges = f"\n<p align='center'>\n\
  <img src='https://img.shields.io/badge/Maintained-Yes-green?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/actions/workflow/status/HeCodes2Much/archlinux.repo.063240.xyz/pages/pages-build-deployment?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/last-commit/HeCodes2Much/archlinux.repo.063240.xyz?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/repo-size/HeCodes2Much/archlinux.repo.063240.xyz?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/static/v1?label=Packages&message={pkgcount}&colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/license/HeCodes2Much/archlinux.repo.063240.xyz?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/issues/HeCodes2Much/archlinux.repo.063240.xyz?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/stars/HeCodes2Much/archlinux.repo.063240.xyz?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/forks/HeCodes2Much/archlinux.repo.063240.xyz?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
  <img src='https://img.shields.io/github/commit-activity/m/HeCodes2Much/archlinux.repo.063240.xyz?colorA=434c5e&colorB=ff59f9&style=flat-square'>\n\
</p>\n"

readme.write(badges)
readme.write(f"\n## Software\n")


def get_file_name(file):
    global name
    head = "head -n5"
    awk = "awk '{$1=$2=\"\"; print $0}'"

    try:
        with open(file, "rb") as fh:
            dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
            stream_reader = dctx.stream_reader(fh)
            text_stream = io.TextIOWrapper(stream_reader, encoding="utf-8")
            for line in text_stream:
                if line.startswith("pkgname"):
                    command = (
                        f"echo '{line}' | {head} | grep -I pkgname | {awk} | sed -n 1p"
                    )
                    process = subprocess.Popen(
                        command, stdout=subprocess.PIPE, stderr=None, shell=True
                    )
                    output = process.communicate()
                    name = str(output[0].decode()).strip()
    except UnicodeDecodeError:
        pass
    except UnboundLocalError:
        pass

    if not name:
        get_file_name(file)
    else:
        return name


def get_file_version(file):
    global version
    head = "head -n5"
    awk = "awk '{$1=$2=\"\"; print $0}'"
    try:
        with open(file, "rb") as fh:
            dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
            stream_reader = dctx.stream_reader(fh)
            text_stream = io.TextIOWrapper(stream_reader, encoding="utf-8")
            for line in text_stream:
                if line.startswith("pkgver"):
                    command = (
                        f"echo '{line}' | {head} | grep -I pkgver | {awk} | sed -n 1p"
                    )
                    process = subprocess.Popen(
                        command, stdout=subprocess.PIPE, stderr=None, shell=True
                    )
                    output = process.communicate()
                    version = str(output[0].decode()).strip()
    except UnicodeDecodeError:
        pass
    except UnboundLocalError:
        pass

    if not version:
        get_file_version(file)
    else:
        return version


def get_file_date(file):
    file_date = os.path.getmtime(file)
    return str(time.strftime("%H:%M:%S %d-%m-%Y", time.localtime(file_date)))


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

    userpac = "<p> <span class='red'>[</span> <span class='yellow'>arch</span><span class='green'>@</span><span class='purple'>linuxrepos.org</span> <span class='red'>~]</span> <br> <span class='green'>pacman</span> <span class='orange'>-Si</span>"
    pacgrep = "<span class='purple'>|</span> <span class='green'>grep</span> <span class='yellow'>'Name\|Version\|Installed\|Build'</span> <span class='purple'>|</span> <span class='green'>awk</span> <span class='orange'>-F</span><span class='yellow'>':' '{print $2}'<span> <span class='purple'>|</span> <span class='green'>sed</span> <span class='yellow'>':a;N;$!ba;s/\\n/ |/g'</span><br>"

    readme.write(
        f"{userpac} <span class='foreground'><a href='docs/{name}'>{name}</a></span> {pacgrep} <span class='foreground'><a href='docs/{name}'>{name} \t|\t {version} \t|\t {size} \t|\t {date}</a></span> </p>\n"
    )

    installme.write(f"{name}\n")
    data.append(f"{name}")

multiline_addrepo = (
    f"\n## Add my repo\n"
    f"* **Maintainer:** [HeCodes2Much](https://aur.archlinux.org/account/HeCodes2Much/)\n"
    f"* **Description:**  A repository with some AUR packages that the team uses\n"
    f"* **Upstream page:** https://archlinux.repo.063240.xyz/\n"
    f"* **Key-ID:** 75A3 8DC6 84F1 A0B8 0891  8BCE E30E C2FB FB05 C44F \n"
    f"* **Fingerprint:** [download](http://pgp.net.nz:11371/pks/lookup?op=vindex&fingerprint=on&search=0xE30EC2FBFB05C44F)\n"
    f"\nAppend to */etc/pacman.conf*:\n```\n[linuxrepos]\nSigLevel = Required DatabaseOptional\nServer = https://archlinux.repo.063240.xyz/$arch/\n```"
    f"\nTo check signature, add my key:\n"
    f"```\nsudo pacman-key --keyserver hkp://pgp.net.nz --recv-key 75A38DC684F1A0B808918BCEE30EC2FBFB05C44F\nsudo pacman-key --keyserver hkp://pgp.net.nz --lsign-key 75A38DC684F1A0B808918BCEE30EC2FBFB05C44F\n```"
    # f"\nYou may also want to \nAppend to */etc/pacman.conf*:\n```\n[linuxrepos-git]\nSigLevel = Optional TrustAll\nServer = https://github.com/HeCodes2Much/archlinux.repo.063240.xyz/releases/download/$repo/\n```"
)

readme.write(multiline_addrepo)

multiline_showsupport = (
    f"\n## Show your support\n"
    f"\nGive a ⭐️ if this project helped you!\n"
    f"\nThis README was generated with ❤️ by [HeCodes2Much](https://github.com/HeCodes2Much/)\n"
    f"*   Last updated on: {datetime}\n"
)

readme.write(multiline_showsupport)

readme.close()
shutil.copyfile("../README.md", "../repo.md")

json_string = json.dumps(data, indent=4)
with open("../packages.json", "w") as outfile:
    outfile.write(json_string)
