from os import system
from colorama import Fore
from time  import sleep
from random import choice , uniform
def IntroMain():
    def typing(staticStr , strObj):
        for i in range(len(strObj)):
            staticStr+=strObj[i]
            sleep(uniform(0.05 , 0.1))
            system("clear")
            print(staticStr)


    banner=f"""{Fore.LIGHTGREEN_EX}\n       (\n    () |\                                  _\n    <==|=@ ⤍                              (o)\n    [\ |/                                 /|\\\n    ||`(                                 / | \\\n    LL \n{Fore.RESET}"""
    spltLines=[]
    for i in banner.split("\n") : spltLines.append(list(i))
    for i in range(len(spltLines)):
        for j in range(len(spltLines[i])-1):
            if spltLines[i][j-1] == '⤍':
                swp=spltLines[i][j]
                spltLines[i][j]=spltLines[i][j-1]
                spltLines[i][j-1]=swp
            strList=''
            system("clear")
            strings = '\n'.join([ "".join(x) for x in spltLines])
            print(strings)
            sleep(0.005)
    colors=[Fore.LIGHTBLUE_EX , Fore.LIGHTCYAN_EX , Fore.LIGHTGREEN_EX , Fore.LIGHTMAGENTA_EX , Fore.LIGHTRED_EX , Fore.LIGHTYELLOW_EX]
    banner=f"""
.▄▄ ·  ▄▄· ▄▄▄  ▪   ▄▄▄·▄▄▄▄▄ ▄▄▄· ▄▄▄   ▄▄·  ▄ .▄▄▄▄ .▄▄▄  
▐█ ▀. ▐█ ▌▪▀▄ █·██ ▐█ ▄█•██  ▐█ ▀█ ▀▄ █·▐█ ▌▪██▪▐█▀▄.▀·▀▄ █·
▄▀▀▀█▄██ ▄▄▐▀▀▄ ▐█· ██▀· ▐█.▪▄█▀▀█ ▐▀▀▄ ██ ▄▄██▀▐█▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█▐███▌▐█•█▌▐█▌▐█▪·• ▐█▌·▐█ ▪▐▌▐█•█▌▐███▌██▌▐▀▐█▄▄▌▐█•█▌
 ▀▀▀▀ ·▀▀▀ .▀  ▀▀▀▀.▀    ▀▀▀  ▀  ▀ .▀  ▀·▀▀▀ ▀▀▀ · ▀▀▀ .▀  ▀
 """
    for i in range(10):
        system("clear")
        print(choice(colors)+banner)
        sleep(0.1)
    msg="卐Hello and welcome to the ScriptArcher. 卐\n\n卐GitHub page : https://github.com/AdolfMacro/ScriptArcher  卐 \n\n 卐Author : AdolfMacro(Mani.k)卐\n\n卐Email : m4nikamran@gmail.com  卐\n\n 卐Telegram : https://t.me/manikamran  卐\n\n卐Enter to continue : "
    typing(banner, msg) 
    system("clear")
    input(banner+msg)