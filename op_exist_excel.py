# -*- coding:utf8 -*-

import xlrd
import xlwt
import os
import sys
from xlutils.copy import copy
from itertools import islice
from scan_testcase import dict2List
from scan_testcase import scan_tcst_path

row = 2
col = 0

#从txt文件中读取数据
def loadData(flieName):  
    inFile = open(flieName, 'r') #以只读方式打开某fileName文件  
  
    #定义list，用来存放文件中的数据
    title = []
    api = []    
    elaspe_t = []  
    dur_t = []
    percall_t = []
  
    for line in islice(inFile,1,None):
        if len(line) < 10: #空行，不规范的行
            continue
        else:
            trainingSet = line.split(',') #对于每一行，通过,分割
            title.append(trainingSet[0])
            api.append(trainingSet[1])
            elaspe_t.append(int(trainingSet[5])) # Time  
            dur_t.append(int(trainingSet[6])) # Duration
            percall_t.append(int(trainingSet[7])) # PerCall  
  
    return (title, api, elaspe_t, dur_t, percall_t)

# excel格式
title_style = xlwt.easyxf('font: color-index black, bold on;align: wrap on, vert centre, horiz left;borders: right 2') #黑，加粗，靠右，右边框线条编号2
api_style = xlwt.easyxf('font: color-index black, bold off;align: wrap on, vert centre, horiz left;borders: right 2')
time_style = xlwt.easyxf('font: color-index black, bold off;align: wrap on, vert centre, horiz right',num_format_str='#,##0') #千分位格式
per_call_time_style = xlwt.easyxf('font: color-index black, bold off;align: wrap on, vert centre, horiz right;borders: right 2',num_format_str='#,##0')

g_space = ' '
def write_one_txt(ws, title, api, elaspe_t, dur_t, percall_t):
    global row
    col_tmp = col
    
    # api
    for i in range(0,len(api)):
        ws.write(row+i, col_tmp, g_space * 10 + api[i], api_style)
    
    # elaspe_t
    col_tmp = col_tmp + 1
    for i in range(0,len(elaspe_t)):
        ws.write(row+i, col_tmp, elaspe_t[i], time_style)
    
    # dur_t    
    col_tmp = col_tmp + 1
    for i in range(0,len(dur_t)):
        ws.write(row+i, col_tmp, dur_t[i], time_style)
    
    # percall_t    
    col_tmp = col_tmp + 1
    for i in range(0,len(percall_t)):
        ws.write(row+i, col_tmp, percall_t[i], per_call_time_style)

    # tps    
    col_tmp = col_tmp + 1
    for i in range(0,len(percall_t)):
        if (0 != percall_t[i]):
            tps = round(1000000000.0 / percall_t[i])
            ws.write(row+i, col_tmp, tps, per_call_time_style)
        else:
            ws.write(row+i, col_tmp, 'N/A', per_call_time_style)
        
    row = row+len(api)

def getFileList(path):
    if (path == ""):
        #path = os.getcwd() + '\\txt\\'
        path = os.path.split( os.path.realpath( sys.argv[0] ) )[0]  + '\\txt\\'
    fileList = []
    files = os.listdir(path)
    
    for f in files:
        if(os.path.isfile(path + '\\' + f) and (os.path.splitext(f)[1] == ".txt")):       
      
            fileList.append(path + '\\' + f)
            print f
    return fileList

xls_name = 'pt-model.xls'

def txt2xls(ws,txt_name):
    # get txt path(defaul:py_path\perf_rslt\)
    path = os.path.split( os.path.realpath( sys.argv[0] ) )[0]  + '\\perf_rslt\\'
    txt_path = path + txt_name
    # read txt
    (title,api,elaspe_t,dur_t,percall_t) = loadData(txt_path)
    # write data
    write_one_txt(ws, title[0], api, elaspe_t, dur_t, percall_t)

def xls_write(ws,content,content_type):
    global row
    ws.write(row, col, content, content_type)
    row = row + 1

def pt_rslt_to_xls(test_case_file_path):
    global row
    # open xls
    old = xlrd.open_workbook(xls_name, formatting_info=True)
    wb = copy(old)
    ws = wb.get_sheet(0)
    
    # load testcase 
    retDict = {}
    scan_tcst_path(test_case_file_path,retDict)
    retList = []
    retList = dict2List(retDict,1,retList)
    
    for item in retList:
        print(item.name)
        space = ''
        if (0 < item.level):
            space = g_space * int(item.level)
            xls_write(ws, space + unicode(item.name, "utf-8"), title_style)
        elif (0 == item.level):
            space = g_space * 8
            xls_write(ws, space + unicode(item.name, "utf-8"), title_style)
            txt_name = 'pt_' + item.funcName + '.txt'
            txt2xls(ws,txt_name)
        else:
            print 'level error!'

    # save xls
    wb.save(xls_name)
    
def main():
    pt_test_file = raw_input('请输入cache_pt.tcst路径(D:\\xx\\cache_pt.tcst)：')
    pt_test_file = unicode(pt_test_file, "gbk")

    pt_rslt_to_xls(pt_test_file)


if __name__ == '__main__':
    main()



