#!/usr/bin/python
#-*- coding: utf-8 -*-
from socket import *

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