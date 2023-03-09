---
title: "aurutils"
date: "2023-03-09"
summary: "helper tools for the arch user repository"
---

# Check linuxrepos for download

pacman -Si *linuxrepos/aurutils*
{{< rawhtml >}}
<pre class="highlight">
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/aurutils-12.1-1-any.pkg.tar.zst">aurutils</a>
<b>Version</b>         : 12.1-1
<b>Description</b>     : helper tools for the arch user repository
<b>Architecture</b>    : any
<b>URL</b>             : https://github.com/AladW/aurutils
<b>Licenses</b>        : custom:ISC
<b>Groups</b>          : None
<b>Provides</b>        : None
<b>Depends On</b>      : git  jq  pacutils  curl  perl
<b>Optional Deps</b>   : bash-completion: bash completion
                  zsh: zsh completion
                  devtools: aur-chroot
                  vifm: default pager
                  perl-json-xs: faster JSON serialization
                  ninja: aur-sync ninja support
                  bat: view-delta example script
                  git-delta: view-delta example script
                  setconf: sync-rebuild example script
<b>Conflicts With</b>  : None
<b>Replaces</b>        : None
<b>Download Size</b>   : 110.61 KiB
<b>Installed Size</b>  : 192.54 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Thu 09 Mar 2023 17:21:42 GMT
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</pre>
{{< /rawhtml >}}
## How to install from linuxrepos

pacman -S *linuxrepos/aurutils*
