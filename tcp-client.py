#!/usr/bin/python
#-*- coding: utf-8 -*-
from socket import *
import struct

class TcpClient:
    #测试，连接本机
    HOST='127.0.0.1'
    #设置侦听端口
    PORT=1122 
    BUFSIZ=1024
    ADDR=(HOST, PORT)
    def __init__(self):
        self.client=socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)
        
        '''close时，立即关闭底层socket,避免出现主动关闭一方出现TIME_WAIT状态'''
        #optval = struct.pack("ii",1,0)
        #self.client.setsockopt(SOL_SOCKET, SO_LINGER, optval)

        while True:
            try:
                data=raw_input('>')
                if not data:
                    break

                self.client.send(data)
                print('发送信息到%s：%s' %(self.HOST,data))
                if data.upper()=="QUIT":
                    break            
                data=self.client.recv(self.BUFSIZ)
                if not data:
                    break
                print('从%s收到信息：%s' %(self.HOST,data))
            except KeyboardInterrupt,e:
                print 'Ctrl+C'
                break
            
if __name__ == '__main__':
    client=TcpClient()