import socket;
import sys;

s = socket.socket();
print("Socket created");
port =4567;
s.bind(('',port));
print("Socket bind to %s"%(port));

s.listen(5);
print("Socket is listening...");

while True:
    #Establish a connection with client
    c,addr = s.accept();
    print("Connection from",addr);
