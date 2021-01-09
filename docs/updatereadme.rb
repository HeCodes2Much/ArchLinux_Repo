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

def get_file_version(file, name)
  begin
    command = "pacman -Si therepoclub/#{name}"
    stdin, stdout, stderr, wait_thr = Open3.popen3(command)
    output = stdout.gets(nil)
    link = "<a href='../#{file}'>#{name}</a>"
    version = output.strip.to_s\
    .gsub("Repository","<b>Repository</b>").strip.to_s\
    .gsub("Name","<b>Name</b>").strip.to_s\
    .gsub("           : #{name}","           : #{link}").strip.to_s\
    .gsub("Version","<b>Version</b>").strip.to_s\
    .gsub("Description","<b>Description</b>").strip.to_s\
    .gsub("Architecture","<b>Architecture</b>").strip.to_s\
    .gsub("URL","<b>URL</b>").strip.to_s\
    .gsub("Licenses","<b>Licenses</b>").strip.to_s\
    .gsub("Groups","<b>Groups</b>").strip.to_s\
    .gsub("Provides","<b>Provides</b>").strip.to_s\
    .gsub("Depends On","<b>Depends On</b>").strip.to_s\
    .gsub("Optional Deps","<b>Optional Deps</b>").strip.to_s\
    .gsub("Conflicts With","<b>Conflicts With</b>").strip.to_s\
    .gsub("Replaces","<b>Replaces</b>").strip.to_s\
    .gsub("Download Size","<b>Download Size</b>").strip.to_s\
    .gsub("Installed Size","<b>Installed Size</b>").strip.to_s\
    .gsub("Packager","<b>Packager</b>").strip.to_s\
    .gsub("Build Date","<b>Build Date</b>").strip.to_s\
    .gsub("Validated By","<b>Validated By</b>").strip.to_s

    return version
  rescue => e
    retry
  end
end

open('../README.md', 'w') { |f|
  f.write("")
}

files = Dir["../x86_64/*.pkg.tar.zst"].sort
for file in files
  begin
    ignore = open("../ignorepackages", "r").read
    name = get_file_name(file.to_s)
    if not ignore.include?(name)
      version = get_file_version(file.to_s, name)
      if not name
        name = get_file_name(file.to_s)
      end
      if not version
        version = get_file_name(file.to_s)
      end

      print("File Updated: (#{name})\n")
      open("#{name}/README.md", "w") { |f|
        f.write("# Check therepoclub for download\n
        \npacman -Si *therepoclub/{name}*\n")
      }
      highlight = '<div class="highlight"><pre class="highlight"><text>'
      open("#{name}/README.md", "a") { |f|
        f.write("\n#{highlight}\n")
      }
      open("#{name}/README.md", "a") { |f|
        f.write("#{version}\n")
      }
      text = '</text></pre></div>'
      open("#{name}/README.md", "a") { |f|
        f.write("#{text}\n")
      }
      open("#{name}/README.md", "a") { |f|
        f.write("\n## How to install from therepoclub\n
        \npacman -S *therepoclub/{name}*\n")
      }
    end
  rescue TypeError
    retry
  end
end