from requests import get , ConnectionError , exceptions
from colorama import Fore
from os import system
from os.path import isfile
def clear():
    system("clear")
def mainSubScanner():
    try:
        while 1:
            clear()
            print(Fore.LIGHTRED_EX + r"""
                                       
             \                  /
    _________))                ((__________
   /.-------./\\    \    /    //\.--------.\
  //#######//##\\   ))  ((   //##\\########\\
 //#######//###((  (( 卐 ))  ))###\\########\\
((#######((#####\\  \\  //  //#####))########))
 \##' `###\######\\  \)(/  //######/####' `##/
  )'    ``#)'  `##\`->oo<-'/##'  `(#''     `(
          (       ``\`..'/''       )
                     \""(
                      `- )
                      / /
                     ( /\
                     /\| \
                    (  \
                        )
                       /
                      (
    """ + Fore.RESET)
            while 1:
                try :
                    url = input(f"{Fore.LIGHTCYAN_EX}\n\n[ * ] Enter the url : {Fore.RESET}")
                    get(url)
                    break
                except KeyboardInterrupt: 
                    raise KeyboardInterrupt
                except :    
                    print(f"{Fore.LIGHTRED_EX}[ E ] URL is not valid!{Fore.RESET}")
            domainName=url.replace("https://", "").replace("http://", "").replace("www.", "")
            proto=url.replace(domainName, "").replace("www.", "")
            while 1:
                subDomList = input(f"\n\n{Fore.LIGHTMAGENTA_EX}[ * ] Enter the word list file : {Fore.RESET}")        
                if isfile(subDomList):
                    break
                print(f"{Fore.LIGHTRED_EX}[ E ] File not found!{Fore.RESET}")
            with open(subDomList) as f:
                fcount=0
                tcount=0
                tlist=[]
                for sub in f.read().split("\n"):
                    try:
                        if "200" in str(get(proto+sub+'.'+domainName)):
                            tcount+=1
                            tlist.append(sub+'.'+domainName)
                        else :
                            fcount+=1
                    except ConnectionError: 
                        fcount+=1
                    except exceptions.InvalidURL :
                        fcount+=1
                    
                    clear()
                    print(f"""{Fore.LIGHTGREEN_EX}[ * ] Found subdomains: {tcount}
    {Fore.LIGHTRED_EX}[ ! ] Unsuccessful attempts: {fcount}
    {Fore.LIGHTYELLOW_EX}[ * ] Total efforts: {tcount+fcount}""")
                if tcount :
                    print(f"\n\n{Fore.LIGHTGREEN_EX}Items found: \n\n" + '\n'.join(tlist))
                input(f"{Fore.LIGHTGREEN_EX}\n\n[ * ] Enter to continue : ")
    except KeyboardInterrupt:
        pass