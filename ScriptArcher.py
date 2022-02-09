try :
    from os import system , getuid
except ImportError :
    print("\n\nCan not from os import system and getuid !")
def clear():
    system("clear")
clear()
if getuid() != 0:
    print('''
                  .----.
      .---------. | == |
      |.-"""""-.| |----|
      || X   X || | == |    Error ; this tool must be run as root !
      ||   _   || |----|
      |'-.....-'| |::::|    Use = sudo scriptArcher
      `"")---(""` |___.|
     /:::::::::::\\" _  "
    /:::=======:::\`\`\\
    `"""""""""""""`  '-'
    ''')
    exit()
try:
    import random
except ImportError:
    print("\n\nCan not import random !")
try:
    from colorama import Fore as color
except ImportError:
    print("\n\nCan not from colorama import Fore !")
try:
    from random import randint
except ImportError :
    print("\n\nCan not from random import randint ! ")
try:
    from os import name as OSname, sched_setscheduler
except ImportError:
    print("\n\nCan not from os import name and sched_setscheduler !")
try:
    from tools.network import IPfounder , MassMailerAttack , scan , DDOS ,DeauthenticationAttacks , MacSpoofing  , ArpSpoofing , dBmAnalyzer
except ImportError:
    print("\n\nCan not import ScriptArcher tools")

def randomColor():
    num=randint(0,4)
    if not num:
        return color.LIGHTCYAN_EX
    elif num == 1 :
        return color.LIGHTGREEN_EX
    elif num == 2 :
        return color.LIGHTBLUE_EX
    else :
        return color.LIGHTYELLOW_EX
def update():
    clear()
    print("\n\n\tUpdating ...")

def Help():
    pass
def main():
    clear()
    print(f"""{randomColor()}

            ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗     █████╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗        (
            ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝    ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗       |\\
            ███████╗██║     ██████╔╝██║██████╔╝   ██║       ███████║██████╔╝██║     ███████║█████╗  ██████╔╝       | )
            ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║       ██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██╗    ##-------->
            ███████║╚██████╗██║  ██║██║██║        ██║       ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║       | )
            ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       |/
                                                                                                                   (

            1. IPv6 finder                         8. dBm Analyzer
            
            2. Mass Mailer Attack                  9. Exit
            
            3. Scan                                 

            4. DDoS                                
            
            5. Deauthentication Attacks
            
            6. Mac Spoofing 
            
            7. Arp spoofing

    """)
    selection=input(f"{color.RED}[Network]~>{color.LIGHTGREEN_EX}")
    if selection=="1":
        IPfounder.IPfoundermain()
    elif selection == "2":
        MassMailerAttack.MassMailerAttackMain()
    elif selection == "3":
        scan.scanMainFunc()
    elif selection == "4":
        DDOS.DDOSmainF()
    elif selection == "5":
        DeauthenticationAttacks.DeauthenticationAttacksMainF()
    elif selection == "6":
        MacSpoofing.MacSpoofingMainF()
    elif selection == "7":
        ArpSpoofing.ArpSpoofingMainF()
    elif selection == "8":
        dBmAnalyzer.dBmAnalyzerMainF()
    elif selection=='9':
        exit()
while 1 :
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("""
            BYE
         _.-._
        | | | |_
        | | | | |
        | | | | |
      _ |  '-._ |
      \`\`-.'-._;
       \    '   |
        \  .`  /
         |    |        
        """)
        break;
