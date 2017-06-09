#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import socket

try:
    HOST=''
    PORT=50007
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
except Exception as e:
    print str(e)
    sys.exit(0)

print 'start listen'

client = None
while 1:
    try:
        client,addr=s.accept()
        print 'Connected by',addr
        client.settimeout(6)
        while 1:
                data=client.recv(1024)
                if not data:
                    client.close()
                    print 'empty'
                    break
                print 'c say',data
                recv = 's say ' + data
                client.sendall(recv)
    except Exception as e:
        print str(e)
        break
if client is not None:
    client.close()
s.close()