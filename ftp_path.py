#!/usr/bin/python
#coding:utf-8

import sys,os,ftplib

from sys import argv


from ftp_login import py_login

def py_cwd(ftp, pathname):
   """
   Set the current directory on the server.
   eg:python ftp_path.py host c pathname
   """
   try:  
     ftp.cwd(pathname)
   except ftplib.error_perm:
     print 'ERROR: cannot change path to "%s"' % pathname
     return False  
   return True 

def py_pwd(ftp):
   """
   Return the pathname of the current directory on the server.
   eg:python ftp_path.py host
   """
   try:
     path = ftp.pwd()
   except ftplib.error_perm:
     print 'ERROR: get cur path failed'
     return None
   return path

def py_mkd(ftp, pathname):
   """
   Create a new directory on the server.
   eg:python ftp_path.py host m pathname
   """
   try:
     ftp.mkd(pathname)
   except ftplib.error_perm:
     print 'ERROR: create path %s failed' % pathname
     return False
   return True

def py_rmd(ftp, dirname):
   """
   Remove the directory named dirname on the server.
   eg:python ftp_path.py host r dirname
   """
   try:
     ftp.rmd(dirname)
   except ftplib.error_perm:
     print 'ERROR: delete path %s failed' % dirname
     return False
   return True

if __name__ == '__main__':
    if len(argv) >= 2:
        ftp = py_login(argv[1])
    else:
        print "host can not empty."
        sys.exit(0)
    if len(argv) == 4:
        if ('c' == argv[2]):
          py_cwd(ftp,argv[3])
          path = py_pwd(ftp)
          print "cur path is %s." % path
        elif ('m' == argv[2]):
          py_mkd(ftp,argv[3])
          print "create dir %s success." % argv[3]
        elif ('r' == argv[2]):
          py_rmd(ftp,argv[3])
          print "delete dir %s success." % argv[3]
        else:
          print("args are invalid!")   
    elif len(argv) == 2:
        path = py_pwd(ftp)
        print "cur path is %s." % path
    else:
        print "the num of param is wrong."

    ftp.quit()
    ftp.close()
