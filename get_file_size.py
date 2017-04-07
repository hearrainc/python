#--get_file_size.py
# -*- coding: cp936 -*-
#--获取当前路径下所有文件的大小(单位Byte)
# -*- coding:utf8 -*-
import os 

def GetFileSize():
    filePath=os.getcwd()
    out=open('filesize.txt','w')

    out.write('{0:130s} {1:20s}'.format('FileName','FileSize')+'\n')
  
    for r,ds,fs in os.walk(filePath): 
        for f in fs: 
            #print '%s'% os.path.join(r,f),
            size=os.path.getsize(os.path.join(r,f)) 
            #print '==    %f K'% (size/1024.0)
            sizeStr="%s"% size
            
            #print('{0:100s} {1:20s}'.format(os.path.join(r,f),sizeStr))
            
            out.write('{0:130s} {1:20s}'.format(os.path.join(r,f),sizeStr)+'\n')

    out.close()

if __name__ == '__main__':
    GetFileSize()
