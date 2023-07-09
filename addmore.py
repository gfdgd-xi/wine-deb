#!/usr/bin/env python3
import os
import sys
programPath = os.path.split(os.path.realpath(__file__))[0]  # 返回 string
sysList = sys.argv[1:]
if sys.argv[1] == "--github":
    sysList = sys.argv[2:]
for i in sysList:
    os.system(f"python3 '{programPath}/add.py' '{i}'")
os.chdir(programPath)
lists = []

for i in sysList[1:]:
    lists.append(os.path.basename(i))
#if sys.argv[1] == "--github":
#    exit()
#os.system(f"bash '{programPath}/incremental-updating-packages.sh' '{programPath}'")
#os.system("apt-ftparchive release . > Release")
#os.system("rm Release.gpg")
#os.system("rm InRelease")
#os.system("rm gpg.asc")
#if os.getenv("GPGPASSWORD") != "":
#    os.system("gpg --armor --detach-sign -o Release.gpg Release")
#    os.system("gpg --clearsign -o InRelease Release")
#    os.system("gpg --armor --output gpg.asc --export 3025613752@qq.com")
#else:
#    os.system("gpg --armor --detach-sign -o Release.gpg Release")
#    os.system("gpg --clearsign -o InRelease Release")
#    os.system("gpg --armor --output gpg.asc --export 3025613752@qq.com")
#os.system(f"cd '{programPath}/../apt-packages-websize-program/' ; git add .")
#os.system(f"cd '{programPath}/../apt-packages-websize-program/' ; git commit -m '新增 {lists} 个安装包'")
#os.system(f"cd '{programPath}/../apt-packages-websize-program/' ; git push")
os.system('rm Packages || echo "Failed to remove packages file"')
os.system('rm Packages.gz || echo "Failed to remove packages.gz file"')
os.system('rm Release || echo "Failed to remove release file"')
os.system('rm Release.gpg || echo "Failed to remove release.gpg file"')
os.system('rm InRelease || echo "Failed to remove inrelease file"')
os.system('dpkg-scanpackages --multiversion . > Packages')
os.system('gzip -k -f Packages')
os.system('apt-ftparchive release . > Release')
os.system('gpg --default-key "3025613752@qq.com" --batch --pinentry-mode="loopback" --passphrase="$KEYPASSWORD" -abs -o - Release > Release.gpg || error "failed to sign Release.gpg with gpg "')
os.system('gpg --default-key "3025613752@qq.com" --batch --pinentry-mode="loopback" --passphrase="$KEYPASSWORD" --clearsign -o - Release > InRelease || error "failed to sign InRelease with gpg"')
os.system(f"cd '{programPath}/'; git add . ; git commit -m '新增 {lists} 安装包' ; git push")