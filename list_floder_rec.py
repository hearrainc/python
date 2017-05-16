# -*- coding:utf8 -*-   
  
import os
import platform
import pdb

LINUX = 0
WINDOWS = 1

PATH_SEP = '/'

def PlatformType():
    sysstr = platform.system()
    if(sysstr =="Linux"):        
        return LINUX
    elif(sysstr == "Windows"):
        return WINDOWS
    else:
        print ("Other System")

def SetPathSep():
    global PATH_SEP
    sys_type = PlatformType()
    if(WINDOWS == sys_type):
        PATH_SEP = '\\'

allFileNum = 0

def printPath(level, path):   
    global allFileNum
    
    '''''  
    打印一个目录下的所有文件夹和文件  
    ''' 
    #pdb.set_trace()
    
    # 所有文件夹，第一个字段是次目录的级别   
    dirList = []   
    # 所有文件   
    fileList = []   
    # 返回一个列表，其中包含在目录条目的名称(google翻译)   
    files = os.listdir(path)   
    # 先添加目录级别   
    dirList.append(str(level))   
    for f in files:   
        if(os.path.isdir(path + PATH_SEP + f)):   
            # 排除隐藏文件夹。因为隐藏文件夹过多   
            if(f[0] == '.'):   
                pass  
            else:   
                # 添加非隐藏文件夹   
                dirList.append(f)   
        if(os.path.isfile(path + PATH_SEP + f)):   
            # 添加文件   
            fileList.append(f)   
    # 当一个标志使用，文件夹列表第一个级别不打印   
    i_dl = 0  
    for dl in dirList:   
        if(i_dl == 0):   
            i_dl = i_dl + 1  
        else:   
            # 打印至控制台，不是第一个的目录
            
            ##print '-' * (int(dirList[0])), dl
            
            # 打印目录下的所有文件夹和文件，目录级别+1
            print '+' * (int(dirList[0])), dl            
            printPath((int(dirList[0]) + 1), path + PATH_SEP + dl)
    
    for fl in fileList:   
        # 打印文件
        
        print '+' * (int(dirList[0])), fl
        '''
        filepath = path + PATH_SEP
        filepath = filepath + fl
        print filepath
        '''
        # 随便计算一下有多少个文件   
        allFileNum = allFileNum + 1  
  
if __name__ == '__main__':
    path = raw_input("Enter target path:")
    SetPathSep()
    printPath(1, path)   
    print 'all file nums =', allFileNum  
