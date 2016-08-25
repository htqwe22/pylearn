#! /usr/bin/python
# -*- coding: utf-8 -*-
import socket,select
import time,struct
def socket_create():
    #try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setblocking(False)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("",8888))
    s.listen(3)
    print "server listen ..."
    #except Exception , e:
    #    pass
    return s

def server_run():
    sa = socket_create()
    inputs = [sa]
    num = 0
    while True :
        rs,ws,es=select.select(inputs,[],[],1)
        if not rs:
            print "select time out %d" %num
        for m in rs:
            if m == sa:
                (controlSock, clientAddr) = sa.accept()
                print "get new socket",clientAddr
                num+=1
                inputs.append(controlSock)
            else:
                data = m.recv(1024)
                if  not data:
                    inputs.remove(m)
                    print "client ", m.getsockname() ,"exit!"
                    m.close()
                    num -= 1
                else:
                    recvbyts = bytearray(data)
                    print "get %d bytes" %len(recvbyts), repr(recvbyts)
                    print data
                    m.send(recvbyts)
                    
if __name__ == '__main__':
	server_run()
    
          
        

        

