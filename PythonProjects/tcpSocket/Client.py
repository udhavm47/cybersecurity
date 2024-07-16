import socket
import sys

hostname = socket.gethostbyname(socket.gethostname())
port = 4444
hosttoconnect = sys.argv[1]
porttoconnect = 1234
ClientSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#ClientSock.bind((hostname,port))

def connected():
    try:
        ClientSock.connect((hosttoconnect,porttoconnect))
        return True
    except:
       return False
IsConnected = connected()
if IsConnected:
    print(f"\n Connection Eastablished succesfully between {hostname} and {hosttoconnect} \n")
 #435qweacv
#     clientmsg = ClientSock.recv(1024)
#     print(clientmsg.decode("ascii"))
# if KeyboardInterrupt or (IsConnected == False):
#     ClientSock.close()
#print(f"{hosttoconnect} : {msg.decode('ascii')}")

while IsConnected:
#     message = input(f"{hostname}$ ")
#     #connection.send(message.encode("ascii"));
#     clientmsg = ClientSock.recv(1024)
#     print(f"{hosttoconnect} : {clientmsg.decode("ascii")}")
    msgfromserver = ClientSock.recv(1024)
    print(f"{hosttoconnect}: {msgfromserver.decode("ascii")}")
    clientmsg = input(f"{hostname}$ ")
    #ClientSock.send(1024)
    ClientSock.send(clientmsg.encode("ascii"))
if KeyboardInterrupt:
    ClientSock.close();