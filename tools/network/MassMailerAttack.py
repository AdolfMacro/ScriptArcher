import smtplib
from email.message import EmailMessage
from colorama import Fore as color
from random import randint
from getpass import getpass 
from os import system
from os import name as OSname
def randomColor():
    num=randint(0,4)
    if num == 0:
        return color.LIGHTCYAN_EX
    elif num == 1 :
        return color.LIGHTGREEN_EX
    elif num == 2 :
        return color.LIGHTBLUE_EX
    else :
        return color.LIGHTYELLOW_EX
def MassMailerAttackMain():
    try:
        while 1:
            system("clear")
            print(f"""{randomColor()}
            ███╗   ███╗ █████╗ ███████╗███████╗    ███╗   ███╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ████╗ ████║██╔══██╗██╔════╝██╔════╝    ████╗ ████║██╔══██╗██║██║     ██╔════╝██╔══██╗
            ██╔████╔██║███████║███████╗███████╗    ██╔████╔██║███████║██║██║     █████╗  ██████╔╝
            ██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║╚██╔╝██║██╔══██║██║██║     ██╔══╝  ██╔══██╗
            ██║ ╚═╝ ██║██║  ██║███████║███████║    ██║ ╚═╝ ██║██║  ██║██║███████╗███████╗██║  ██║
            ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝

            ^C to back main menu
            """)
            fileMail=input("\nEnter the recipient file path : ")
            sub=input("\nEnter email subject : ")
            smtpServer=input("\nEnter smtp server addres : ")
            smtpPort=input("\nEnter smtp port number : ")
            myEmail=input("\n\nEnter your Email addres : ")
            myEmailPasswd=getpass()
            try:
                mailContent=input("\nEnter email content (Please enter the ^C to end) :")
                while 1:
                    mailContent+="\n"+input(">")
            except KeyboardInterrupt:
                print("\n\n")

            try :
                with open(fileMail,"r") as f:
                    for emailAddr in f.readlines(): 
                        try:
                            email = EmailMessage()
                            email['from'] = myEmail
                            email['to'] = emailAddr.strip()
                            email['subject'] = sub
                            email.set_content(mailContent)
                            with smtplib.SMTP(host=smtpServer, port=smtpPort) as smtp:
                                smtp.ehlo()
                                smtp.starttls()
                                smtp.login(myEmail, myEmailPasswd)
                                smtp.send_message(email)
                                print(f'\n[✔️]Email was sent => {color.LIGHTRED_EX}{emailAddr}{randomColor()}')
                        except :
                            print(f"\n\n{color.LIGHTRED_EX}Problems to send emails! Please try again.")

            except FileNotFoundError:
                print(f"\n\n{color.LIGHTRED_EX}{fileMail} Not found !")
            except:
                print(f"\n\n{color.LIGHTRED_EX}Problems to send emails! Please try again.")
            
    except KeyboardInterrupt:
        pass
