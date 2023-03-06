# Check linuxrepos for download

pacman -Si *linuxrepos/fdroidserver*

<div class="highlight"><pre class="highlight"><text>
<b>Repository</b>      : linuxrepos
<b>Name</b>            : <a href="../../x86_64/fdroidserver-1:2.2.0-1-any.pkg.tar.zst">fdroidserver</a>
<b>Version</b>         : 1:2.2.0-1
<b>Description</b>     : F-Droid repository management tools
<b>Architecture</b>    : any
<b>URL</b>             : https://gitlab.com/fdroid/fdroidserver
<b>Licenses</b>        : GPL3
<b>Groups</b>          : None
<b>Provides</b>        : None
<b>Depends On</b>      : python  python-pyasn1  python-pyasn1-modules  python-magic  python-requests  python-yaml  python-ruamel-yaml  java-environment  python-pillow  python-vagrant  python-gitpython  python-androguard  python-paramiko  python-qrcode
<b>Optional Deps</b>   : android-sdk: Build apps from source
                  android-sdk-build-tools: Work with apks in the repository
                  android-sdk-platform-tools: Ability to install apps to connected devices
                  android-ndk: Build apps that use native code
                  apache-ant: Build apps using Apache Ant
                  maven: Build apps using Maven
                  gradle: Build apps using Gradle
                  android-support-repository: Build apps using Maven or Gradle that use support libraries
                  git: Download app sources that use git or svn (via git svn)
                  mercurial: Download app sources that use hg
                  bzr: Download app sources that use bzr
                  python-pillow: Resize and manage app icons
                  rsync: Transfer repo files to the web server
                  vagrant: Buildserver virtual machine support
                  virtualbox: Buildserver virtual machine support
                  wordpress: Web repository plugin
<b>Conflicts With</b>  : None
<b>Replaces</b>        : None
<b>Download Size</b>   : 686.53 KiB
<b>Installed Size</b>  : 3084.53 KiB
<b>Packager</b>        : Wayne Wesley <wayne6324@gmail.com>
<b>Build Date</b>      : Wed 22 Feb 2023 15:06:09 GMT
<b>Validated By</b>    : MD5 Sum  SHA-256 Sum  Signature
</text></pre></div>

## How to install from linuxrepos

pacman -S *linuxrepos/fdroidserver*