from requests import get ,exceptions
import socket
from re import findall
from colorama import Fore as color
from os import name , system
def IPfoundermain():
    system("clear")
    ip=socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[1][4][0]
    if ip == '::1':
        print(f'''{color.LIGHTGREEN_EX}
                                                               ~~~~~~           |
         .----.    ____                                   ,o88~~88888888o,      |
       .---------. | == |                                 ,~~?8P  88888   8,    |
       |.-"""""-.| |----|               {color.RED} __    __{color.LIGHTGREEN_EX}      d  d88 d88 d8_88     b   |
       || 0   0 || | == |            _  {color.RED} \ \  / /{color.LIGHTGREEN_EX}     d  d888888888          b  |
       ||   ~   || |----|___________/ |-{color.RED}  \ \/ / {color.LIGHTGREEN_EX}     8,?88888888  d8.b o.   8  |
       |'-.....-'| |::::|           \_|-{color.RED}   |  |   {color.LIGHTGREEN_EX}    8~88888888~ ~^8888\ db 8  |
       `"")---(""` |___.|               {color.RED}  / /\ \ {color.LIGHTGREEN_EX}     ?  888888          ,888P  |
      /:::::::::::\\\\" _  "            {color.RED}   /_/  \_\{color.LIGHTGREEN_EX}           ?  `8888b,_ d888P   |
     /:::=======:::\`\`\\\\                               `   8888888b   ,888'    |
     `"""""""""""""`  '-'                                 ~-?8888888 _.P-~      |
                                                               ~~~~~~           | 
        ''')
        input("\n\nEnter to continue : ")
        return None
    print(f"""{color.LIGHTRED_EX}
    {ip}
    """)
    input("\n\nPleas [Enter] to continue : ")
