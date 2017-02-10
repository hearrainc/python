# --- picknames.py ---
# -*- coding: cp936 -*-
# -*- coding:utf8 -*-

import os

def GetFileList():
    filenames=os.listdir(os.getcwd())
    print filenames
    #for name in filenames:
    #   filenames[filenames.index(name)]=name
    out=open('names.txt','w')
    for name in filenames:
        out.write(name+'\n')
    out.close()

if __name__ == '__main__':
    GetFileList()
