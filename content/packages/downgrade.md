---
title: "downgrade"
date: "2022-10-25"
summary: "Bash script for downgrading one or more packages to a version in your cache or the A.L.A."
---

# Check linuxrepos for download

pacman -Si *linuxrepos/downgrade*
{{< rawhtml >}}
<pre class="highlight">
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/downgrade-11.2.1-1-any.pkg.tar.zst">downgrade</a>
<b>Version</b>         : 11.2.1-1
<b>Description</b>     : Bash script for downgrading one or more packages to a version in your cache or the A.L.A.
<b>Architecture</b>    : any
<b>URL</b>             : https://github.com/archlinux-downgrade/downgrade
<b>Licenses</b>        : GPL
<b>Groups</b>          : None
<b>Provides</b>        : None
<b>Depends On</b>      : pacman-contrib  fzf
<b>Optional Deps</b>   : sudo: for installation via sudo
<b>Conflicts With</b>  : None
<b>Replaces</b>        : None
<b>Download Size</b>   : 36.60 KiB
<b>Installed Size</b>  : 75.12 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Tue 25 Oct 2022 06:56:02 BST
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</pre>
{{< /rawhtml >}}
## How to install from linuxrepos

pacman -S *linuxrepos/downgrade*
