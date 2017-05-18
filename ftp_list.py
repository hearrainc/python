#!/usr/bin/python
#coding:utf-8

import sys
import ftplib
from sys import argv

from ftp_login import py_login

def py_list(ftp,path="/"):
   """
   LIST(list file info in path)
   eg:python ftp_list.py host /uspp
   """
   ftp.cwd(path)
   data = []
   ftp.dir(data.append)

   for line in data:
       print line
       
def py_nlist(ftp,path="/"):
   """
   NLST(list file name in path)
   eg:python ftp_list.py 10.43.214.226 /uspp
   """
   ftp.cwd(path)
   file_list = ftp.nlst()

   for line in file_list:
       print line

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
