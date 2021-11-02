from os import system ,getuid
import sys
if getuid() != 0:
    print('''
                  .----.
      .---------. | == |
      |.-"""""-.| |----|
      || X   X || | == |    Error ; this tool must be run as root !
      ||   _   || |----|
      |'-.....-'| |::::|    Use = sudo python3 install.py
      `"")---(""` |___.|
     /:::::::::::\\" _  "
    /:::=======:::\`\`\\
    `"""""""""""""`  '-'
    ''')
    exit()
from sys import path
try :
    import scapy
except ImportError :
    if input("\nCan not find scapy , install it [Y/n]? ").lower() == "y":
        errcode = system("pip3 install scapy")
        if errcode:
            errcode = system("pip install scapy")
            if errcode:
                print("\n\nError can not use python3-pip ; please install it and try agin ...")
try:
    import email
except ImportError :
    if input("\nCan not find email library , install it [Y/n]? ").lower() == "y":
        errcode = system("pip3 install email")
        if errcode:
            errcode = system("pip install email")
            if errcode:
                print("\n\nError can not use python3-pip ; please install it and try agin ...")
errcode = system("nmap")
if errcode:
    with open("/etc/os-release","r") as distro:
        if "debian" or "Debian" in distro.read():
            system("apt-get install nmap")
        elif "redhat" or "RedHat" or "fedora" or "CentOS" or "centos" in distro.read():
            system("yum install nmap")
        elif  "arch" or "Arch" or "Manjaro" or "manjaro" :
            errcode = system("snap install nmap")
            if errcode:
                system("pacman -S snapd")
                system("systemctl enable --now snapd.socket")
                system("ln -s /var/lib/snapd/snap /snap")
                system("snap install nmap")
errcode = system("mkdir /usr/src/scriptarcher/")
if errcode:
    errcode =system("mkdir /usr/src/ScriptArcher/")
    pathF="/usr/src/ScriptArcher/"
    if errcode:
        errcode = system("mkdir /usr/src/ScriptArcher1/")
        pathF="/usr/src/ScriptArcher1/"
        if errcode:
            dirname=input("\n\nCan not making 'scriptarcher' , 'ScriptArcher' and 'ScriptArcher1' in /usr/src/ . \bEnter the file name please : ")
            errcode=system(f"mkdir /usr/src/{dirname}/")
            if errcode:
                print("Error in making dir please try agin ! ")
try :
    system(f"cp {path[0]}/ScriptArcher.py {pathF} ; cp -R {path[0]}/tools/ {pathF}")
    system(f"echo 'python3 {pathF}/ScriptArcher.py' > /usr/local/bin/scriptarcher")
    system("chmod +x /usr/local/bin/scriptarcher")
except NameError:
    system(f"cp {path[0]}/ScriptArcher.py /usr/src/scriptarcher/; cp -R {path[0]}/tools/ /usr/src/scriptarcher/")
    system(f"echo 'python3 /usr/src/scriptarcher/ScriptArcher.py' > /usr/local/bin/scriptarcher")
    system("chmod +x /usr/local/bin/scriptarcher")
