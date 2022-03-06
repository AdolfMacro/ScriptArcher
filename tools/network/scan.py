from os import system
from os import  name as OSname
from colorama import Fore as color
from subprocess import CalledProcessError, check_output
from random import randint
from os import system
from os import name as OSname
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
def scanMainFunc():
    try:
        while 1:
            system("clear")
            print(f"""{randomColorF()}
                    ███████╗ ██████╗ █████╗ ███╗   ██╗
                    ██╔════╝██╔════╝██╔══██╗████╗  ██║
                    ███████╗██║     ███████║██╔██╗ ██║
                    ╚════██║██║     ██╔══██║██║╚██╗██║
                    ███████║╚██████╗██║  ██║██║ ╚████║
                    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

                1. Port scanning        6. Zombie scan

                2. IP scanning          7. Half open scan

                3. IP range scanning    8. Exit

                4. Scan popular ports

                5. Sweep Network
            """)
            selection=input(f"{randomColorF()}[Scan]~> ")
            if selection == "1":
                host=input("\nEnter host : ")
                while 1:
                    rangePort=input("\n\nEnter port range (start-stop) : ")
                    split=rangePort.split('-')
                    if len(split)==2:
                        if not int(split[0]) <=65534:
                            print("\nValue error . try agin ...")
                        elif not int(split[0]) <=65535:
                            print("\nValue error . try agin ...")
                        else :
                            break
                    else:
                        print("\nValue error . try agin ...")
                saveToFile=input("\n\nSave output to file [N/y] : ").lower()
                if saveToFile=='y':
                    fileName=input("\nEnter file name : ")
                    check_output(f"nmap -p {rangePort} {host} -o {fileName}", shell=True, universal_newlines=True)
                else:
                    returned_text = check_output(f"nmap -p {rangePort} {host}", shell=True, universal_newlines=True)
                    print("\n\n"+returned_text+"\n\n")
                    input("\n\nEnter to continue :")
            elif selection=="2":
                host=input("\nEnter host : ")
                saveToFile=input("\n\nSave output to file [N/y] : ").lower()
                if saveToFile=='y':
                    fileName=input("\nEnter file name : ")
                    check_output(f"nmap {host} -o {fileName}", shell=True, universal_newlines=True)
                else:
                    returned_text = check_output(f"nmap {host}", shell=True, universal_newlines=True)
                    print("\n\n"+returned_text+"\n\n")
                    input("\n\nEnter to continue :")
            elif selection=="3":
                host=input("\nEnter host (like '192.168.1.' ): ")
                saveToFile=input("\n\nSave output to file [N/y] : ").lower()
                if saveToFile=='y':
                    fileName=input("\nEnter file name : ")
                    check_output(f"nmap -sp {host}* -o {fileName}", shell=True, universal_newlines=True)
                else:
                    returned_text=check_output(f"nmap -sp {host}*", shell=True, universal_newlines=True)
                    print("\n\n"+returned_text+"\n\n")
                    input("\n\nEnter to continue :")
            elif selection=="4":
                host=input("\nEnter host : ")
                number=input("\nEnter number of ports : ")
                saveToFile=input("\n\nSave output to file [N/y] : ").lower()
                if saveToFile=='y':
                    fileName=input("\nEnter file name : ")
                    check_output(f"nmap --top-ports {number} {host} -o {fileName}", shell=True, universal_newlines=True)
                else:
                    returned_text=check_output(f"nmap –top-ports {number} {host}", shell=True, universal_newlines=True)
                    print("\n\n"+returned_text+"\n\n")
                    input("\n\nEnter to continue :")
            elif selection=="5":
                host=input("\nEnter host : ")
                netmask=input("\nEnter host netmask (default =24) : ")
                if not netmask:
                    netmask="24"
                saveToFile=input("\n\nSave output to file [N/y] : ").lower()
                if saveToFile=='y':
                    fileName=input("\nEnter file name : ")
                    check_output(f"nmap -sn {host}/{netmask} -o {fileName}", shell=True, universal_newlines=True)
                else:
                    returned_text=check_output(f"nmap -sn {host}/{netmask}", shell=True, universal_newlines=True)
                    print("\n\n"+returned_text+"\n\n")
                    input("\n\nEnter to continue :")
            elif selection=="6":
                Thost=input("\nEnter target ip : ")
                Zhost=input("\nEnter zombie ip : ")
                while 1:
                    try:
                        Zport=int(input("\nEnter zombie port : "))
                        Tport=int(input("\nEnter target port : "))
                        break
                    except ValueError:
                        print("\n[!] Value Error !\n\n")
                saveToFile=input("\n\nSave output to file [N/y] : ").lower()
                command=f"nmap -Pn -p{Tport} -sI {Zhost}:{Zport} {Thost}"                
                if saveToFile=='y':
                    fileName=input("\nEnter file name : ")
                    command+=f" -o {fileName}"
                
                returned_text=check_output(command, shell=True, universal_newlines=True)
                print("\n\n"+returned_text+"\n\n")
                input("\n\nEnter to continue :")
            elif selection=="7":
                host=input("\nEnter ip : ")        
                saveToFile=input("\n\nSave output to file [N/y] : ").lower()
                if saveToFile=='y':
                    fileName=input("\nEnter file name : ")
                    check_output(f"nmap -sS {host} -o {fileName}", shell=True, universal_newlines=True)
                else:
                    returned_text=check_output(f"nmap -sS {host}", shell=True, universal_newlines=True)
                    print("\n\n"+returned_text+"\n\n")
                    input("\n\nEnter to continue :")
            elif selection=="8":
                break
    except CalledProcessError :
        print("Somthing was wrong pleas try agin ... ")
        input("\n\nEnter to continue : ")
