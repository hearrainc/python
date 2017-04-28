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

def py_list(ftp,path="/"):
   ftp.cwd(path)
   data = []
   ftp.dir(data.append)

   for line in data:
       print "-",line


if __name__ == '__main__':
    if len(argv) >= 2:
        ftp = py_login(argv[1])
    else:
        print "host can not empty."
        sys.exit(0)

    if len(argv) == 3:
        py_list(ftp,argv[2])
    elif len(argv) == 2:
        py_list(ftp)
    else:
        print "param too much."

    ftp.quit()
    ftp.close()
