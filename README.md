## socket

##### 交互图

1. TCP
![tcp](./tcp.jpg)

2. UDP

![udp](./udp.jpg)

##### 导入方法
import socket 或 from socket import *
***
##### socket接口使用例子
**.listen(backlog)** *开始监听TCP传入连接。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了，并不是指最大客户端连接数。*

**.sendall(string[,flag])** *完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常*

**.recvfrom(bufsize[.flag])** *接受UDP套接字的数据*

**.sendto(string[,flag],address)** *发送UDP数据*

等等
*** 

##### 多线程实现的例子

1. 创建一个Thread的server端，使用telnet连接

[server(thread).py](./server(thread).py)

2. 创建一个Threading的server端，和与之对应的client端

[server(threading).py](./server(threading).py)

[client(follow-threading).py](./client(follow-threading).py)
