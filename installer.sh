
echo -E """
         ___           _        _ _           
        |_ _|_ __  ___| |_ __ _| | | ___ _ __ 
         | || '_ \/ __| __/ _\` | | |/ _ \ '__|
         | || | | \__ \ || (_| | | |  __/ |   
        |___|_| |_|___/\__\__,_|_|_|\___|_|
        _____________________________________
    Installer for ScriptArcher tool , Start installation
    
"""

pip3 install scapy
pip3 install colorama
pip3 install contextlib
pip3 install email
pip3 install getpass
pip3 install requests

release=$(egrep '^ID_LIKE=' /etc/os-release)
if [[ $release == *"arch"* ]]; then
  sudo pacman -S net-tools --noconfirm
  sudo pacman -S nmap --noconfirm
  sudo pacman -S aircrack-ng  --noconfirm
fi
if [[ $release == *"debian"* ]]; then
  sudo apt-get --assume-yes install net-tools
  sudo apt-get --assume-yes install nmap
  sudo apt-get --assume-yes install aircrack-ng
fi

if [[ $release == *"rhel"* ]]; then
  yum -y install net-tools
  yum -y install nmap
  yum -y install aircrack-ng
fi

sudo -u root mkdir /usr/src/scriptarcher/
line="$0"
replace="installer.sh"
replacewith=""
temp=$( realpath "$0"  )
line=$(dirname "$temp")
replace="/tools"
replacewith=""
line="${line/${replace}/${replacewith}}"
echo $line
sudo -u root cp -R $line/* /usr/src/scriptarcher/
sudo sh -c 'echo "python3 /usr/src/scriptarcher/ScriptArcher.py" > /usr/local/bin/scriptarcher'
sudo -u root chmod +x /usr/local/bin/scriptarcher
echo """
██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║  ██║██║   ██║██╔██╗ ██║█████╗  
██║  ██║██║   ██║██║╚██╗██║██╔══╝  
██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""