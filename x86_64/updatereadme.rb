# coding: utf-8
require 'date'
require 'active_support/core_ext/integer/inflections'
require 'open3'
require 'open-uri'
require 'json'

def get_file_name(file)
  begin
    awk1 = "awk '{print $0}'"
    awk2 = "awk '{$1=$2=\"\"; print $0}'"
    command = "bsdtar -xOf #{file} | #{awk1} | grep -I pkgname | #{awk2}"
    stdin, stdout, stderr, wait_thr = Open3.popen3(command)
    output = stdout.gets(nil)
    return output.strip.to_s
  rescue => e
    retry
  end
end

def get_file_version(file)
  begin
    awk1 = "awk '{print $0}'"
    awk2 = "awk '{$1=$2=\"\"; print $0}'"
    command = "bsdtar -xOf #{file} | #{awk1} | grep -I pkgver | #{awk2}"
    stdin, stdout, stderr, wait_thr = Open3.popen3(command)
    output = stdout.gets(nil)
    return output.strip.to_s
  rescue => e
    retry
  end
end

def get_aur_name(name)
  begin
    packages = []
    response = URI.open("https://aur.archlinux.org/rpc/?v=5&type=search&arg=#{CGI.escape(name)}").read
    data = JSON.parse(response)
    
    title = data["results"]
    title.each do |title|
      new_name = title["Name"]
      packages.push(new_name)
    end

    if packages.include?("#{name}")
      return "#{name}"
    elsif packages.include?("#{name}-git")
      return "#{name}-git"
    elsif packages.include?("#{name}-bin")
      return "#{name}-bin"
    else
      return "#{name}"
    end
  rescue => e
    retry
  end
end

open("../README.md", "w") { |f|
  f.write("")
}
home = Dir.home
open("#{home}/.config/package-list", "w") { |f|
  f.write("")
}

badges = ("# <img src='favicon.ico'> The Repo Club's Arch Repo <img src='favicon.ico'>\n
<p align='center'>\n\
  <img src='https://img.shields.io/badge/Maintained-Yes-green?color=red&style=flat-square'>\n\
  <img src='https://img.shields.io/github/last-commit/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square'>\n\
  <img src='https://img.shields.io/github/repo-size/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square'>\n\
  <img src='https://img.shields.io/static/v1?label=License&message=CC%20BY-NC-SA%204.0&color=red&style=flat-square'>\n\
  <img src='https://img.shields.io/github/issues/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square'>\n\
  <img src='https://img.shields.io/github/stars/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square'>\n\
  <img src='https://img.shields.io/github/forks/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square'>\n\
  <img src='https://img.shields.io/github/commit-activity/m/TheCynicalTeam/Arch.TheRepo.Club?color=red&style=flat-square'>\n\
</p>
\n## Software\n")

open("../README.md", "a") { |f|
  f.write(badges)
}

files = Dir["*.pkg.tar.zst"].sort
for file in files
  begin
    ignore = open("../ignorepackages", "r").read
    name = get_file_name(file.to_s)
    if not ignore.include?(name)
      version = get_file_version(file.to_s)
      if not name
        name = get_file_name(file.to_s)
      end
      if not version
        version = get_file_name(file.to_s)
      end

      print("File Updated: (#{name} v#{version})\n")
      aur_name = "#{get_aur_name(name)}"
      open("../README.md", "a") { |f|
        f.write("*   [#{name}](docs/#{name}/) Version: #{version} ![AUR maintainer](https://img.shields.io/aur/maintainer/#{aur_name}?color=blue&style=flat-square) ![AUR maintainer](https://img.shields.io/aur/license/#{aur_name}?color=orange&style=flat-square)\n")
      }
      open("#{home}/.config/package-list", "a") { |f|
        f.write("#{name} #{version}\n")
      }
    end
  rescue TypeError
    retry
  end
end

multiline_addrepo = ("\n## Add my repo\n"\
"* **Maintainer:** [TheCynicalTeam](https://aur.archlinux.org/account/TheCynicalTeam/)\n"\
"* **Description:**  A repository with some AUR packages that the team uses\n"\
"* **Upstream page:** https://arch.therepo.club/\n"\
"* **Key-ID:** 10DF 44AC D4C8 4539 53B7 CCBA 206A DED6 6160 901B\n"\
"* **Fingerprint:** [download](http://pgp.net.nz:11371/pks/lookup?op=vindex&fingerprint=on&search=0x96414492E2220753)\n"\
"\nAppend to */etc/pacman.conf*:\n```\n[therepoclub]\nSigLevel = Required DatabaseOptional\nServer = https://arch.therepo.club/$arch/\n```"\
"\nTo check signature, add my key:\n"\
"```\nsudo pacman-key --keyserver hkp://pgp.net.nz --recv-key 75A38DC684F1A0B808918BCEE30EC2FBFB05C44F\nsudo pacman-key --keyserver hkp://pgp.net.nz --lsign-key 75A38DC684F1A0B808918BCEE30EC2FBFB05C44F\n```")

open("../README.md", "a") { |f|
  f.write(multiline_addrepo)
}

d = Time.new
dt = DateTime.now.strftime("Last updated on: %a #{d.day.ordinalize}, %b %Y at %I:%M:%S%p")

multiline_showsupport = ("\n## Show your support\n"\
"\nGive a ⭐️ if this project helped you!\n"\
"\nThis README was generated with ❤️ by [TheCynicalTeam](https://github.com/TheCynicalTeam/)\n"\
"*   #{dt}")

open("../README.md", "a") { |f|
  f.write(multiline_showsupport)
}
