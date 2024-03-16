# Check linuxrepos for download

pacman -Si *linuxrepos/pikaur*

<div class="highlight"><pre class="highlight"><text>
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/pikaur-1.18.4-1-any.pkg.tar.zst">pikaur</a>
<b>Version</b>         : 1.18.4-1
<b>Description</b>     : AUR helper which asks all questions before installing/building. Inspired by pacaur, yaourt and yay.
<b>Architecture</b>    : any
<b>URL</b>             : https://github.com/actionless/pikaur
<b>Licenses</b>        : GPL3
<b>Groups</b>          : None
<b>Provides</b>        : pikaur
<b>Depends On</b>      : pyalpm  git
<b>Optional Deps</b>   : devtools: for Arch Pkgs support in -G/--getpkgbuild operation
                  python-pysocks: for socks5 proxy support
                  python-defusedxml: securely wrap Arch news replies
<b>Conflicts With</b>  : pikaur-git
<b>Replaces</b>        : None
<b>Download Size</b>   : 410.34 KiB
<b>Installed Size</b>  : 1860.98 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Sat 09 Mar 2024 12:54:28 UTC
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</text></pre></div>

## How to install from linuxrepos

pacman -S *linuxrepos/pikaur*
