#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import thread
from time import sleep
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #add and port reuse
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' > ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
print '开始'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data_recv = conn.recv(1024)
        data = data_recv.replace("\r\n","")
        reply = 'OK...' + data
        
        print repr(data)
        if not data: 
            break
     
        conn.sendall(reply)

    #came out of loop
    conn.shutdown(2)
    conn.close()
 
#now keep talking with the client
while True:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    thread.start_new_thread(clientthread ,(conn,))
    sleep(10)   #wait thread end
    break

s.shutdown(2)
s.close()