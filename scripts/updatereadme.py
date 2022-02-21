import glob
import subprocess
import os
import json
import errno
from parse_pacman import parse_pacman


def filebrowser(ext=""):
    "Returns files with an extension"
    return [file for file in glob.glob(f"../x86_64/*{ext}")]

files = filebrowser(".pkg.tar.zst")

files.sort()

def get_file_name(file):
    head = "head -n5"
    awk = "awk '{$1=$2=\"\"; print $0}'"
    command = f"bsdtar -xOf {file} .BUILDINFO | {head} | grep -I pkgname | {awk} | sed -n 1p"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    name = str(output[0].decode()).strip()

    if not name:
        get_file_name(file)
    else:
        return name

def get_file_version(file):
    head = "head -n5"
    awk = "awk '{$1=$2=\"\"; print $0}'"
    command = f"bsdtar -xOf {file} .BUILDINFO | {head} | grep -I pkgver | {awk} | sed -n 1p"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
    version = str(output[0].decode()).strip()

    if not version:
        get_file_version(file)
    else:
        return version

def get_file_info(file, name):
    command = f"pacman -Si therepoclub/{name}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()
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

    res = {}
    k = ""
    for l in output[0].decode().splitlines():
        if len(l) == 0: continue
        if l[0] != ' ':
            r = l.split(':')
        else:
            r = []
            r.append(k)
            r.extend(l.split(':'))
        if len(r) == 2:
            vr = r[1].strip().split("  ")
            if len(vr) == 1: vr = vr[0]
        else:
            if r[2][0] != ' ':
                vr = ':'.join(r[1:]).strip().split("  ")
                if len(vr) == 1: vr = vr[0]
            else:
                v = r[2].strip().split("  ")
                if len(v) == 1: v = v[0]
                vr = {}
                vr[r[1].strip()] = v
        k = r[0].strip()
        if k in res:
            res[k][list(vr.keys())[0]] = list(vr.values())[0]
        else:
            res[k] = vr

    output = json.dumps(res, sort_keys=True, indent=2)
    with open(f"../json/{name}.json", 'w') as outfile:
        outfile.write(output)

    if not version:
        get_file_info(file, name)
    else:
        return fileInfo
    

for file in files:
    name = str(get_file_name(file))
    name = str(get_file_name(file))
    version = str(get_file_version(file))
    info = str(get_file_info(file, name))

    print(f"File Updated: Name ({name}), Version ({version})")
    file_name = f'../docs/{name}/README.md'
    if not os.path.exists(os.path.dirname(file_name)):
        os.makedirs(os.path.dirname(file_name))
    readme = open(file_name, 'w+')
    readme.write(f"# Check therepoclub for download\n")
    readme.write(f"\npacman -Si *therepoclub/{name}*\n")
    highlight = '<div class="highlight"><pre class="highlight"><text>'
    readme.write(f"\n{highlight}\n")
    readme.write(f"{info}")
    text = '</text></pre></div>'
    readme.write(f"\n{text}\n")
    readme.write(f"\n## How to install from therepoclub\n")
    readme.write(f"\npacman -S *therepoclub/{name}*\n")
    readme.close()

if os.path.exists(os.path.dirname('../docs/None/README.md')):
    os.remove('../docs/None/README.md')
    os.rmdir(os.path.dirname('../docs/None/README.md'))
