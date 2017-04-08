#!/usr/bin/python
#coding:utf-8

import sys
import ftplib
from sys import argv

def py_login(host,user="test",pwd="test"):
    "ftp login"
    py_ftp = ftplib.FTP(host)
    py_ftp.login(user,pwd)
    return py_ftp
    
if __name__ == '__main__':
    if len(argv) >= 2:
        ftp = py_login(argv[1])
        print "welcome ftp(host:%s)." % argv[1]
    else:
        print "host can not empty."
        sys.exit(0)

    ftp.quit()
    ftp.close()
