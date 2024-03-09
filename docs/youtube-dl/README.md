# Check linuxrepos for download

pacman -Si *linuxrepos/youtube-dl*

<div class="highlight"><pre class="highlight"><text>
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/youtube-dl-2021.12.17-2-any.pkg.tar.zst">youtube-dl</a>
<b>Version</b>         : 2021.12.17-2
<b>Description</b>     : A command-line program to download videos from YouTube.com and a few more sites
<b>Architecture</b>    : any
<b>URL</b>             : https://ytdl-org.github.io/youtube-dl/
<b>Licenses</b>        : custom
<b>Groups</b>          : None
<b>Provides</b>        : None
<b>Depends On</b>      : python
<b>Optional Deps</b>   : ffmpeg: for video post-processing
                  rtmpdump: for rtmp streams support
                  atomicparsley: for embedding thumbnails into m4a files
                  python-pycryptodome: for hlsnative downloader
<b>Conflicts With</b>  : None
<b>Replaces</b>        : None
<b>Download Size</b>   : 3.99 MiB
<b>Installed Size</b>  : 18.03 MiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Sat 16 Sep 2023 19:39:55 UTC
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</text></pre></div>

## How to install from linuxrepos

pacman -S *linuxrepos/youtube-dl*
