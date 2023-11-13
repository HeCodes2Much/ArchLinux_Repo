# Check linuxrepos for download

pacman -Si *linuxrepos/clifm*

<div class="highlight"><pre class="highlight"><text>
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/clifm-1.15-1-x86_64.pkg.tar.zst">clifm</a>
<b>Version</b>         : 1.15-1
<b>Description</b>     : The command line file manager
<b>Architecture</b>    : x86_64
<b>URL</b>             : https://github.com/leo-arch/clifm
<b>Licenses</b>        : GPL2
<b>Groups</b>          : None
<b>Provides</b>        : clifm
<b>Depends On</b>      : libcap  readline  acl  file
<b>Optional Deps</b>   : archivemount: Archives mount
                  atool: Archives/compression support
                  p7zip: ISO 9660 support
                  cdrtools: ISO 9660 support
                  fzf: fzf mode for TAB completion
                  smenu: smenu mode for TAB completion
                  udevil: (un)mount storage devices
                  udisks2: (un)mount storage devices
<b>Conflicts With</b>  : None
<b>Replaces</b>        : None
<b>Download Size</b>   : 585.98 KiB
<b>Installed Size</b>  : 1364.20 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Mon 13 Nov 2023 08:31:42 GMT
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</text></pre></div>

## How to install from linuxrepos

pacman -S *linuxrepos/clifm*
