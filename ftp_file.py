#!/usr/bin/python
#coding:utf-8

import sys
import ftplib
from sys import argv

from ftp_login import py_login

def py_rename(ftp,fromname,toname):
   """
   Rename file fromname on the server to toname
   eg:python ftp_file.py host fromname toname
   """
   if -1 == fromname.find("/"):
      srcfile = ftp.pwd() + '/' + fromname
   if -1 == toname.find("/"):
      dstfile = ftp.pwd() + '/' + toname
   else:
      srcfile = fromname
      dstfile = toname
   ret = ftp.rename(fromname,toname)

def py_delete(ftp,filename):
   """
   Remove the file named filename from the server
   eg:python ftp_file.py host filename
   """
   ftp.delete(filename)
       
def py_size(ftp,filename):
   """
   Request the size of the file named filename on the server,
   eg:python ftp_file.py host filename
   """
   if -1 == filename.find("/"):
      file_path = ftp.pwd() + '/' + filename
   else:
      file_path = filename
   size = ftp.size(file_path)
   print "file size = %d" % size

if __name__ == '__main__':
    if len(argv) >= 2:
        ftp = py_login(argv[1])
    else:
        print "host can not empty."
        sys.exit(0)
    if len(argv) == 3:
        py_delete(ftp,argv[2])
    elif len(argv) == 4:
        py_rename(ftp,argv[2],argv[3])
    else:
        print "the num of param is wrong."

    ftp.quit()
    ftp.close()
