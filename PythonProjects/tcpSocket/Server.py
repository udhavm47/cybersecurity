import socket;

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 1234
sock.bind((host,port));
sock.listen(1);
print(F"\nServer Started at {host}\n")
#connection, addr = sock.accept();
#sock.connect((host,4444))
#print(f"\n Connected to {addr} ")
(connection,addr) = sock.accept();
while True:
   msgfromserver = input(f"{host}$ ")
   connection.send(msgfromserver.encode("ascii"))
   msgrcv = connection.recv(1024);
   print(f"{addr[0]}: {msgrcv.decode("ascii")}")
#    if KeyboardInterrupt:
#       break
# sock.close()
   