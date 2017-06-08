#!/usr/bin/python
#-*- coding: utf-8 -*-
from socket import *
from time import ctime
from time import localtime
import time
import struct

HOST=''
PORT=1122  #设置侦听端口

BUFSIZ=1024
ADDR=(HOST, PORT)

sock=socket(AF_INET, SOCK_STREAM)

'''close时，立即关闭底层socket'''
#optval = struct.pack("ii",1,0)
#sock.setsockopt(SOL_SOCKET, SO_LINGER, optval)

sock.bind(ADDR)

sock.listen(5)
#设置退出条件
STOP_CHAT=False
while not STOP_CHAT:
    tcpClientSock = None
    print('等待接入，侦听端口:%d' % (PORT))
    try:
        tcpClientSock, addr=sock.accept()
        print '接受连接，客户端地址:',addr
        while True:
            try:
                data=tcpClientSock.recv(BUFSIZ)
            except:
                #print(e)
                tcpClientSock.close()
                break
            if not data:
                break
            #python3使用bytes，所以要进行编码
            #s='%s发送给我的信息是:[%s] %s' %(addr[0],ctime(), data.decode('utf8'))
            #对日期进行一下格式化
            ISOTIMEFORMAT='%Y-%m-%d %X'
            stime=time.strftime(ISOTIMEFORMAT, localtime())
            s='%s发送给我的信息是:%s' %(addr[0],data)
            tcpClientSock.send(s)
            print([stime], ':', data)
            #如果输入quit(忽略大小写),则程序退出
            STOP_CHAT=(data.upper()=="QUIT")
            if STOP_CHAT:
                break
    except KeyboardInterrupt,e:
        print 'Ctrl+C'
        break
if tcpClientSock is not None:
    tcpClientSock.close()
sock.close()