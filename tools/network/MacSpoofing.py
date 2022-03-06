from os import system
from time import sleep
from subprocess import call
def MacSpoofingMainF():
    while 1:
        try:
            system("clear")
            print("""
    ███╗   ███╗ █████╗  ██████╗    ███████╗██████╗  ██████╗  ██████╗ ███████╗██╗███╗   ██╗ ██████╗
    ████╗ ████║██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝██║████╗  ██║██╔════╝
    ██╔████╔██║███████║██║         ███████╗██████╔╝██║   ██║██║   ██║█████╗  ██║██╔██╗ ██║██║  ███╗
    ██║╚██╔╝██║██╔══██║██║         ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝  ██║██║╚██╗██║██║   ██║
    ██║ ╚═╝ ██║██║  ██║╚██████╗    ███████║██║     ╚██████╔╝╚██████╔╝██║     ██║██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝
            \n\n      """)
            ifc=input("\nEnter the interface : ")
            Smac=input("\nPlease enter mac to spoof : ")
            try :
                call(['sudo', 'ifconfig', ifc, 'down'])
                call(['sudo', 'ifconfig', ifc, 'hw', 'ether', Smac])
                call(['sudo', 'ifconfig', ifc, 'up'])
            except Exception as e:
                print(f"\n\n[ ! ] {e}\n\n")
            Exit=input("\n\nDone !\n\nExit from MAC SPOOFING [N/y] ?").lower()
            if Exit=="y":
                break
        except KeyboardInterrupt:
            break
