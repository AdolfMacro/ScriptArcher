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
            ifc=input("\nEnter the interface (Must be in monitoring mode) : ")
            print("\n_.~-> Please enter the fox to exit the scan <-~._")
            sleep(2)
            system(f"airodump-ng {ifc}")
            Tmac=input("\n\n\nPlease enter the target mac : ")
            Smac=input("\nPlease enter mac to spoof : ")
            try :
                sub.call(['sudo', 'ifconfig', interface, 'down'])
                sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
                sub.call(['sudo', 'ifconfig', interface, 'up'])
            except :
                print("\n\nProblem executing commands. Check the values and then try again\n\n")
            Exit=input("\n\nDone !\n\nExit from MAC SPOOFING [N/y] ?").lower()
            if Exit=="y":
                break
        except KeyboardInterrupt:
            break
