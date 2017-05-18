#!/usr/bin/python
#coding:utf-8

import sys,os,ftplib

from sys import argv

from ftp_login import py_login

from ftp_path import py_cwd

CONST_BUFFER_SIZE = 4096

def py_upload(ftp, localpath, remotepath='/'):
   """
   Retrieve a file in binary transfer mode from the server
   eg:python ftp_up+down.py host p localpath [remotepath]
   """
   if False == os.path.exists(localpath):
     print 'file "%s" is not exist' % localpath
     return False
   f = open(localpath, "rb")
   file_name = os.path.split(localpath)[-1]  
   try:
     py_cwd(ftp,remotepath)
     ftp.storbinary('STOR %s' % file_name, f, CONST_BUFFER_SIZE)
   except ftplib.error_perm:
     print 'ERROR: cannot write file "%s"' % filename
     return False  
   return True 

def py_download(ftp, filepath):
   """
   Store a file in binary transfer mode from the server
   eg:python ftp_up+down.py host g filename
   """
   file_name = os.path.split(filepath)[-1] 
   f = open(file_name,"wb")
   try:  
     ftp.retrbinary("RETR %s" % filepath, f.write, CONST_BUFFER_SIZE)
     f.close()
   except ftplib.error_perm:
     os.remove(file_name)
     print 'ERROR: cannot read file "%s"' % filepath
     return False  
   return True


if __name__ == '__main__':
    if len(argv) >= 2:
        ftp = py_login(argv[1])
    else:
        print "host can not empty."
        sys.exit(0)
    if len(argv) >= 4:
        if ( 'p' == argv[2] ):
          if len(argv) == 4:
            py_upload(ftp,argv[3])
          elif len(argv) == 5:
            py_upload(ftp,argv[3],argv[4])
        elif( 'g' == argv[2] ):
          py_download(ftp,argv[3])
        else:
          print("args are invalid!")
    else:
        print "the num of param is wrong."

    ftp.quit()
    ftp.close()
