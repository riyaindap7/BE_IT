import socket
s=socket.socket()
s.bind(('localhost',8567))
s.listen(1)
print("waiting to connect")
while True:
    c,addr=s.accept()
    print("Connected to",addr)
    c.send(bytes("Heyclient",'utf-8'))
    while True:
        file_recieved=c.recv(1024).decode()
        print(file_recieved)
         
        if not file_recieved:
            break
    print("file recieved")
    c.close()
