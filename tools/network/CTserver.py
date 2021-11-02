import socket
from os import system 
def CTserverMainF():
    while 1:
        try:
            system("clear")
            print("""

             ██████╗██╗     ██╗███████╗███╗   ██╗████████╗
            ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝
            ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║
            ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║
            ╚██████╗███████╗██║███████╗██║ ╚████║   ██║
             ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝
                  """)
            Sip=input("\n\nEnter the server IP : ")
            while 1:
                try:
                    Sport=int(input("\nEnter the server port : "))
                    break
                except ValueError:
                    print("\n\nValueError !\n")
            client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect((Sip,Sport))
            print(f"\n[*] Connected to {Sip}:{Sport}")
            while 1:
                message=input("\nEnter your message : ")
                client.send(bytes(message,flags="utf8"))
                recv=client.recv(1024)
                print(f"[*] Recv message from client : {recv.decode()}")
        except KeyboardInterrupt:
            break
        except OSError:
            print("Error ! Please check the entered values then try again\n\n Enter to continue")
