# Check linuxrepos for download

pacman -Si *linuxrepos/nemo-compare*

<div class="highlight"><pre class="highlight"><text>
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/nemo-compare-5.8.0-1-x86_64.pkg.tar.zst">nemo-compare</a>
<b>Version</b>         : 5.8.0-1
<b>Description</b>     : Context menu comparison extension for Nemo file manager
<b>Architecture</b>    : x86_64
<b>URL</b>             : https://github.com/linuxmint/nemo-extensions
<b>Licenses</b>        : GPL3
<b>Groups</b>          : nemo-extensions
<b>Provides</b>        : None
<b>Depends On</b>      : nemo-python>=3.9.0  python-gobject
<b>Optional Deps</b>   : meld: Install at least one file comparison program
                  kompare: Additional comparison options (preferred diff, three-way, multi-compare)
                  fldiff: Additional comparison options (preferred diff, three-way, multi-compare)
                  diffuse: Alternate comparison backend
                  kdiff3: Alternate comparison backend
<b>Conflicts With</b>  : None
<b>Replaces</b>        : None
<b>Download Size</b>   : 20.00 KiB
<b>Installed Size</b>  : 18.08 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Mon 26 Jun 2023 18:55:16 UTC
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</text></pre></div>

## How to install from linuxrepos

pacman -S *linuxrepos/nemo-compare*
