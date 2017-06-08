#!/usr/bin/python

from socket import *
import struct

class Client():
    def __init__(self):
        self.tcpCliSock=socket(AF_INET,SOCK_STREAM)
        self.tcpCliSock.connect(('127.0.0.1',9990))
        
        '''close时，立即关闭底层socket'''
        optval = struct.pack("ii",1,0)
        self.tcpCliSock.setsockopt(SOL_SOCKET, SO_LINGER, optval)
        
        print 'connect server successfully !'
        #self.cf = self.tcpCliSock.makefile('rw', 0)

    def work(self):
        while True:
            try:
                data=raw_input('>')
                if data:
                    #self.cf.write(data+"\n")
                    self.tcpCliSock.send(data)
                    if data.upper() == 'QUIT':
                        break
                    #data = self.cf.readline().strip()
                    self.tcpCliSock.recv(1024)
                    if data:
                        print "server say:",data
                    else:
                        break
                else:
                    break   
            except Exception,e:
                print "send error,",str(e)
                break

        self.tcpCliSock.close()
        print "close connect."
if __name__ == "__main__":  
    cl = Client()
    cl.work()