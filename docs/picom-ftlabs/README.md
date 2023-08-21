# Check linuxrepos for download

pacman -Si *linuxrepos/picom-ftlabs*

<div class="highlight"><pre class="highlight"><text>
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/picom-ftlabs-2023.08.16-1-x86_64.pkg.tar.zst">picom-ftlabs</a>
<b>Version</b>         : 2023.08.16-1
<b>Description</b>     : picom fork by FT-Labs including animations (git-version)
<b>Architecture</b>    : x86_64
<b>URL</b>             : https://github.com/FT-Labs/picom
<b>Licenses</b>        : MIT  MPL2
<b>Groups</b>          : None
<b>Provides</b>        : compton  compton-git  picom
<b>Depends On</b>      : libgl  libev  pcre  libx11  xcb-util-renderutil  libxcb  xcb-util-image  libxext  pixman  libconfig  libdbus  hicolor-icon-theme
<b>Optional Deps</b>   : dbus: To control picom via D-Bus
                  xorg-xwininfo: For picom-trans
                  xorg-xprop: For picom-trans
                  python: For picom-convgen.py
<b>Conflicts With</b>  : compton  compton-git  picom
<b>Replaces</b>        : compton-git
<b>Download Size</b>   : 239.70 KiB
<b>Installed Size</b>  : 488.37 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Mon 21 Aug 2023 22:20:47 BST
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</text></pre></div>

## How to install from linuxrepos

pacman -S *linuxrepos/picom-ftlabs*
