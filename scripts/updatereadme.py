import glob
import subprocess
import os
import io
import json
import shutil
import zstandard
from parse_pacman import parse_pacman
from datetime import datetime


def deletefile(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def filebrowser(ext=""):
    "Returns files with an extension"
    return [file for file in glob.glob(f"../static/x86_64/*{ext}")]


files = filebrowser(".pkg.tar.zst")

files.sort()


def get_file_name(file):
    global name
    head = "head -n5"
    awk = "awk '{$1=$2=\"\"; print $0}'"

    try:
        with open(file, 'rb') as fh:
            dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
            stream_reader = dctx.stream_reader(fh)
            text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
            for line in text_stream:
                if line.startswith('pkgname'):
                    command = f"echo '{line}' | {head} | grep -I pkgname | {awk} | sed -n 1p"
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
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
        with open(file, 'rb') as fh:
            dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
            stream_reader = dctx.stream_reader(fh)
            text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
            for line in text_stream:
                if line.startswith('pkgver'):
                    command = f"echo '{line}' | {head} | grep -I pkgver | {awk} | sed -n 1p"
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
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


def get_file_info(file, name):
    command = f"pacman -Si linuxrepos/{name}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    file = file.replace("static/", "")
    link = f'<a href="../{file}">{name}</a>'
    fileInfo = str(output[0].decode())\
    .replace("Repository","<b>Repository</b>").strip()\
    .replace("Name","<b>Name</b>").strip()\
    .replace(f"           : {name}",f"           : {link}").strip()\
    .replace("Version","<b>Version</b>").strip()\
    .replace("Description","<b>Description</b>").strip()\
    .replace("Architecture","<b>Architecture</b>").strip()\
    .replace("URL","<b>URL</b>").strip()\
    .replace("Licenses","<b>Licenses</b>").strip()\
    .replace("Groups","<b>Groups</b>").strip()\
    .replace("Provides","<b>Provides</b>").strip()\
    .replace("Depends On","<b>Depends On</b>").strip()\
    .replace("Optional Deps","<b>Optional Deps</b>").strip()\
    .replace("Conflicts With","<b>Conflicts With</b>").strip()\
    .replace("Replaces","<b>Replaces</b>").strip()\
    .replace("Download Size","<b>Download Size</b>").strip()\
    .replace("Installed Size","<b>Installed Size</b>").strip()\
    .replace("Packager","<b>Packager</b>").strip()\
    .replace("Build Date","<b>Build Date</b>").strip()\
    .replace("Validated By","<b>Validated By</b>").strip()

    res = parse_pacman(output[0].decode())

    output = json.dumps(res, sort_keys=True, indent=2)
    with open(f"../static/json/{name}.json", 'w') as outfile:
        outfile.write(output)

    if not fileInfo:
        get_file_info(file, name)
    else:
        return fileInfo


def get_build_date(file):
    global date
    head = "head -n5"
    awk = "awk '{$1=$2=\"\"; print $0}'"
    try:
        with open(file, 'rb') as fh:
            dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
            stream_reader = dctx.stream_reader(fh)
            text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
            for line in text_stream:
                if line.startswith('builddate'):
                    command = f"echo '{line}' | {head} | grep -I builddate | {awk} | sed -n 1p"
                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
                    output = process.communicate()
                    date = int(str(output[0].decode()).strip())
    except UnicodeDecodeError:
        pass
    except UnboundLocalError:
        pass

    if not date:
        get_build_date(file)
    else:
        # Converting timestamp to DateTime object
        datetime_object = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
        return datetime_object


def get_build_info(file, name):
    global test
    command = f"pacman -Si linuxrepos/{name} | grep 'Description'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    fileInfo = str(output[0].decode())\
        .replace("Description     : ","").strip()

    if not fileInfo:
        get_build_info(file, name)
    else:
        return fileInfo


deletefile(f"../content/packages/")
deletefile(f"../static/json/")

for file in files:
    name = str(get_file_name(file))
    version = str(get_file_version(file))
    info = str(get_file_info(file, name))
    build = str(get_build_date(file))
    summary = str(get_build_info(file, name))

    header = f"""---
title: \"{name}\"
date: \"{build}\"
summary: \"{summary}\"
---"""

    print(f"File Updated: Name ({name}), Version ({version})")
    file_name = f'../content/packages/{name}.md'
    if not os.path.exists(os.path.dirname(file_name)):
        os.makedirs(os.path.dirname(file_name))
    readme = open(file_name, 'w+')
    readme.write(f"{header}\n\n")
    readme.write(f"# Check linuxrepos for download\n")
    readme.write(f"\npacman -Si *linuxrepos/{name}*\n")
    readme.write("{{< rawhtml >}}")
    highlight = '<pre class="highlight">'
    readme.write(f"\n{highlight}\n")
    readme.write(f"{info}")
    text = '</pre>'
    readme.write(f"\n{text}\n")
    readme.write("{{< /rawhtml >}}")
    readme.write(f"\n## How to install from linuxrepos\n")
    readme.write(f"\npacman -S *linuxrepos/{name}*\n")
    readme.close()
