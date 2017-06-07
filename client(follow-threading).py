#!/usr/bin/python

from socket import *
import struct

class Client():
    def __init__(self):
        pass

    def work(self):
        tcpCliSock=socket(AF_INET,SOCK_STREAM)
        tcpCliSock.connect(('127.0.0.1',9990))
        
        '''close时，立即关闭底层socket'''
        optval = struct.pack("ii",1,0)
        tcpCliSock.setsockopt(SOL_SOCKET, SO_LINGER, optval)
        
        print 'connect server successfully !'
        cf = tcpCliSock.makefile('rw', 0)
        while True:
            try:
                data=raw_input('>')
                if data:
                    cf.write(data+"\n")
                    if data.upper() == 'QUIT':
                        break
                    data = cf.readline().strip()
                    if data:
                        print "server say:",data
                    else:
                        break
                else:
                    break   
            except Exception,e:
                print "send error,",str(e)
                break
        
        #tcpCliSock.shutdown(2)
        tcpCliSock.close()
        
        print "close connect."
if __name__ == "__main__":  
    cl = Client()
    cl.work()