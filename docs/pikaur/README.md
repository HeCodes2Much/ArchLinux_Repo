# Check linuxrepos for download

pacman -Si *linuxrepos/pikaur*

<div class="highlight"><pre class="highlight"><text>
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/pikaur-1.29.1-1-any.pkg.tar.zst">pikaur</a>
<b>Version</b>         : 1.29.1-1
<b>Description</b>     : AUR helper which asks all questions before installing/building. Inspired by pacaur, yaourt and yay.
<b>Architecture</b>    : any
<b>URL</b>             : https://github.com/actionless/pikaur
<b>Licenses</b>        : GPL-3.0-only
<b>Groups</b>          : None
<b>Provides</b>        : pikaur
<b>Depends On</b>      : pyalpm  git
<b>Optional Deps</b>   : devtools: for Arch Pkgs support in -G/--getpkgbuild operation
                  python-pysocks: for socks5 proxy support
                  python-defusedxml: securely wrap Arch news replies
                  pacman-contrib: to use in pacman hook/systemd timer for cleaning up pikaur cache
<b>Conflicts With</b>  : pikaur-git
<b>Replaces</b>        : None
<b>Download Size</b>   : 490.05 KiB
<b>Installed Size</b>  : 1932.61 KiB
<b>Packager</b>        : HeCodes2Much <wayne6324@gmail.com>
<b>Build Date</b>      : Fri 27 Sep 2024 10:56:06 BST
<b>Validated By</b>    : SHA-256 Sum
</text></pre></div>

## How to install from linuxrepos

pacman -S *linuxrepos/pikaur*
