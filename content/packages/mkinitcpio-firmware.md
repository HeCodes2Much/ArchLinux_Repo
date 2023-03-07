---
title: "mkinitcpio-firmware"
date: "2022-12-24"
summary: "Optional firmware for the default linux kernel to get rid of the annoying 'WARNING: Possibly missing firmware for module:' messages"
---

# Check linuxrepos for download

pacman -Si *linuxrepos/mkinitcpio-firmware*
{{< rawhtml >}}
<pre class="highlight">
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../static/x86_64/mkinitcpio-firmware-1.4.0-1-any.pkg.tar.zst">mkinitcpio-firmware</a>
<b>Version</b>         : 1.4.0-1
<b>Description</b>     : Optional firmware for the default linux kernel to get rid of the annoying 'WARNING: Possibly missing firmware for module:' messages
<b>Architecture</b>    : any
<b>URL</b>             : https://aur.archlinux.org/packages/mkinitcpio-firmware
<b>Licenses</b>        : GPL
<b>Groups</b>          : None
<b>Provides</b>        : None
<b>Depends On</b>      : linux-firmware  aic94xx-firmware  ast-firmware  linux-firmware-qlogic  linux-firmware-bnx2x  linux-firmware-liquidio  linux-firmware-mellanox  linux-firmware-nfp  wd719x-firmware  upd72020x-fw
<b>Optional Deps</b>   : mkinitcpio: build the initramfs
                  linux: default linux preset
<b>Conflicts With</b>  : None
<b>Replaces</b>        : None
<b>Download Size</b>   : 13.91 KiB
<b>Installed Size</b>  : 0.23 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Sat 24 Dec 2022 12:21:37 GMT
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</pre>
{{< /rawhtml >}}
## How to install from linuxrepos

pacman -S *linuxrepos/mkinitcpio-firmware*
