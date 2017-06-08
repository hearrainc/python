#!/usr/bin/python

import os,time
from socket import *
import threading

import struct

class Server():
    def __init__(self,host='',port=9990):
        try:
            addr=(host,port)
            self.tcpSerSock=socket(AF_INET,SOCK_STREAM)
            self.tcpSerSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
            self.tcpSerSock.bind(addr)
            self.tcpSerSock.listen(2)
        except Exception,e :  
            print 'ip or port error :',str(e)
            self.tcpSerSock.close()

    def main(self):
        while True:
            try:
                print 'wait for connecting ...'
                tcpCliSock,addr = self.tcpSerSock.accept()
                addrStr = addr[0]+':'+str(addr[1])
                print 'connect from ',addrStr
            except KeyboardInterrupt:
                self.close=True
                tcpCliSock.close()
                self.tcpSerSock.close()
                print 'KeyboardInterrupt'
                break
            ct = ClientThread(tcpCliSock,addrStr)
            ct.start()

class ClientThread(threading.Thread):
    def __init__(self,tcpClient,addr):
        super(ClientThread,self).__init__()

        self.tcpClient = tcpClient
        self.addr = addr
        self.timeout = 60
        tcpClient.settimeout(self.timeout)
          
    def run(self):
        while 1:
            try:
                
                data=self.tcpClient.recv(1024)
                if data:
                    if data.find("set time")>=0:
                        self.timeout = int(data.replace("set time ",""))
                        self.tcpClient.settimeout(self.timeout)
                    if data.upper() == "QUIT":
                        print self.addr," quit"
                        break
                    print self.addr,"client say:",data
                    #self.cf.write(str(self.addr)+" recevied ok!"+"\n")
                    self.tcpClient.send(str(self.addr)+" recevied ok!")
                else:
                    break
            except Exception,e:
                #self.tcpClient.send('time out.')
                print self.addr,str(e)
                self.tcpClient.close()
                break

        self.tcpClient.close()
        print '%s over' % self.getName()
if __name__ == "__main__" :  
    ser = Server()
    ser.main()