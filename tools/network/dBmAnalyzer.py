import subprocess
from re import findall
from os import system
from time import sleep
# sudo iw dev wlp8s0 scan | egrep “BSS\|signal\|SSID”
def dBmAnalyzerMainF():
    while 1:
        try:
            iface=input("\n\nEnter the interface : ")
            Eloop=False
            while 1:
                try:
                    printStr=""
                    sleep(0.5)
                    process = subprocess.Popen(['iw', 'dev',iface,'scan'],
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    Cout=stdout.decode()
                    if stderr:
                        system("clear")
                        print("\n\nValueError !\n\nPlease check the entered values and try again\n")
                        break
                    BSS=findall(r".*BSS (.*)\(" , Cout)
                    SSID=findall(r".*SSID: (.*)" , Cout)
                    signal=findall(r"signal: (.*)" , Cout)
                    for i in range(len(BSS)):
                        printStr+="\n"+BSS[i]+"\t"+SSID[i]+"\t"+signal[i]
                        print(printStr)
                    system("clear")
                    print("""
               .              .
            .´  ·  .      .  ·  `.
            :  :  :  (¯)  :  :   :
            `.  ·  ` /¯\\ ´  ·  .´
                    /¯¯¯\\

Enter ^C to Exit ...""")
                    print("\nSSID\t\t\tBSS\t\tSignal\n")
                    print(printStr)
                except KeyboardInterrupt:
                    Eloop=True
                    break
        except KeyboardInterrupt:
            break
        if Eloop:
            break
