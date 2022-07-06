try :
    from os import system , getuid
    from sys import argv
except ImportError :
    print("\n\nCan not from os import system and getuid !")
    exit()
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
    from colorama import Fore as color
except ImportError:
    print("\n\nCan not from colorama import Fore !")
    exit()
from random import randint
try:
    from tools.network import IPfounder , MassMailerAttack , scan , DDOS ,DeauthenticationAttacks , MacSpoofing  , ArpSpoofing , dBmAnalyzer
    from tools.intro import IntroMain
    from tools.web import subScanner
except ImportError as e:
    print(f"\n\nCan not import ScriptArcher tools\n\n[ E ] {e}")
    exit()


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
    if not "-nb" in argv :
        IntroMain()
    while True:
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
            
            2. Mass Mailer Attack                  9. Subdomain scanner
            
            3. Scan                                10. Exit

            4. DDoS                                
            
            5. Deauthentication Attacks
            
            6. Mac Spoofing 
            
            7. Arp spoofing

        """)
        selection=input(f"{color.RED}[ScriptArcher]~>{color.LIGHTGREEN_EX}")
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
        elif selection=="9":
            subScanner.mainSubScanner()
        elif selection=='10':
            exit()

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
    exit()
