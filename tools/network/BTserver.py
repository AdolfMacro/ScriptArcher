import socket
from os import system
def BTserverMainF():
    while 1:
        try:
            system("clear")
            print("""
            ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗
            ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
            ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
            ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
            ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
            ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
            \n\n""")
            bip=input("\n\nEnter the ip : ")
            while 1:
                try:
                    bport=int (input("\nEnter the port : "))
                    break
                except ValueError:
                    print("\n\nValueError !\n")

            while 1:
                try:
                    listenNumber=int(input("\nEnter the listen number : "))
                    break
                except ValueError:
                    print("\n\nValueError !\n")

            server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            server.bind((bip,bport))
            server.listen(listenNumber)
            print(f"\n[*] Start listening on {bip}:{bport}")
            while 1:
                client,addr=server.accept()
                print(f"[*] Accepted connection from : {addr[0]}:{addr[1]}")
                message=client.recv(1024)
                print(f"[*] Recv message from client : {message.decode()}")
                client.send(bytes(input("\nEnter your message : "),encoding='utf8'))
        except KeyboardInterrupt:
            break
        except OSError:
            print("Error ! Please check the entered values then try again\n\n Enter to continue")
