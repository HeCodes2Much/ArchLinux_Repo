# Check linuxrepos for download

pacman -Si *linuxrepos/kernel-install-mkinitcpio*

<div class="highlight"><pre class="highlight"><text>
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/kernel-install-mkinitcpio-1.5-1-any.pkg.tar.zst">kernel-install-mkinitcpio</a>
<b>Version</b>         : 1.5-1
<b>Description</b>     : A framework for enabling systemd-boot automation using kernel-install with mkinitcpio
<b>Architecture</b>    : any
<b>URL</b>             : https://gitlab.com/dalto.8/eos-systemd-boot
<b>Licenses</b>        : GPL2
<b>Groups</b>          : None
<b>Provides</b>        : None
<b>Depends On</b>      : systemd  mkinitcpio
<b>Optional Deps</b>   : None
<b>Conflicts With</b>  : dracut  kernel-install-for-dracut
<b>Replaces</b>        : None
<b>Download Size</b>   : 14.24 KiB
<b>Installed Size</b>  : 18.13 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Sat 26 Aug 2023 17:01:38 UTC
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</text></pre></div>

## How to install from linuxrepos

pacman -S *linuxrepos/kernel-install-mkinitcpio*
