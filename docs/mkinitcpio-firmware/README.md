# Check linuxrepos for download

pacman -Si *linuxrepos/mkinitcpio-firmware*

<div class="highlight"><pre class="highlight"><text>
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/mkinitcpio-firmware-1.3.0-2-any.pkg.tar.zst">mkinitcpio-firmware</a>
<b>Version</b>         : 1.3.0-2
<b>Description</b>     : Optional firmware for the default linux kernel to get rid of the annoying 'WARNING: Possibly missing firmware for module:' messages
<b>Architecture</b>    : any
<b>URL</b>             : https://aur.archlinux.org/packages/mkinitcpio-firmware
<b>Licenses</b>        : GPL
<b>Groups</b>          : None
<b>Provides</b>        : None
<b>Depends On</b>      : linux-firmware  aic94xx-firmware  linux-firmware-qlogic  linux-firmware-bnx2x  linux-firmware-liquidio  linux-firmware-mellanox  linux-firmware-nfp  wd719x-firmware  upd72020x-fw
<b>Optional Deps</b>   : mkinitcpio: build the initramfs
                  linux: default linux preset
<b>Conflicts With</b>  : None
<b>Replaces</b>        : None
<b>Download Size</b>   : 17.34 KiB
<b>Installed Size</b>  : 0.23 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Wed 06 Jul 2022 07:00:29 BST
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</text></pre></div>

## How to install from linuxrepos

pacman -S *linuxrepos/mkinitcpio-firmware*
