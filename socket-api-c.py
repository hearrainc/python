#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket

try:
    HOST='127.0.0.1'
    PORT=50007
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
except Exception as e:
    print str(e)
    
while 1:
    try:
        cmd=raw_input("Please input>")
        s.sendall(cmd)
        data=s.recv(1024)
        print data
    except KeyboardInterrupt,e:
        print str(e)
        break
s.close()