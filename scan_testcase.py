#coding:utf-8
import re
import collections
import json
import os.path
import xml.etree.ElementTree as ET

keys = [
    "cache_connect_db_by_index",
    "cache_connect_db_by_handle",
    "cache_connect_db_by_handle_ex"
]


def decoding(content, coding_from="gb2312", coding_to="utf-8"):
    return content.decode(coding_from).encode(coding_to)


def get_func_name_from_cdap_req(msg):
    content = str(decoding(msg.text, coding_from="utf-8", coding_to="ascii")).strip().decode("hex").strip()
    #tree = ET.ElementTree()
    #parse = ET.XMLParser(recover=True)
    content = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", content)
    tree = ET.fromstring(content)
    jsonContent = tree.find("content").get("value")
    jsonDecoder = json.JSONDecoder()
    jsonDict = jsonDecoder.decode(jsonContent)
    funcName = jsonDict["cache_test_perf"]["name"]
    if isinstance(funcName, unicode):
        funcName = str(funcName)
    return funcName


def scan_fcas_path(file_name, retDict):
    dirpath, name = os.path.split(file_name)
    with open(file_name) as f:
        content = f.read().replace("gb2312", "utf-8")
        content = decoding(content, "gb2312", "utf-8")
    try:
        root = ET.XML(content)
        preCondSet =  root.find("PreCondSet").findall("NetInterInst")
        MessageFlowSet = root.find("MessageFlow").findall("NetInterInst")
    except AttributeError:
        print(u"文件错误， 文件名=%s", file_name)
        return False

    for inst in preCondSet:
        if inst.get("SimpleDesp") in keys:
            retDict[name] = get_func_name_from_cdap_req(inst.findall("Message")[0])
            return True

    for inst in MessageFlowSet:
        if inst.get("SimpleDesp") in keys:
            retDict[name] = get_func_name_from_cdap_req(inst.findall("Message")[0])
            return True

    return False


def scan_tcst_path(file_name, retDict):
    dirpath, name = os.path.split(file_name)
    valDict = collections.OrderedDict()
    with open(file_name) as f:
        content = f.read().replace("gb2312", "utf-8")
        content = decoding(content, "gb2312", "utf-8")

    try:
        root = ET.XML(content)
        #testCaseSet = root.find("TestCaseSet")
        testCaseSet = root.findall("TestCaseSetR")
        testCaseFunc = root.findall("FuncTestCase")
    except AttributeError:
        print(u"文件错误， 文件名=%s", file_name)
        return False
    for caseSet in testCaseSet:
        leafCaseName = caseSet.get("FilePath")
        scan_tcst_path(dirpath + "\\" + leafCaseName, valDict)

    for caseFunc in testCaseFunc:
        leafCaseName = caseFunc.get("FilePath")
        scan_fcas_path(dirpath + "\\" + leafCaseName, valDict)

    retDict[name] = valDict
    return True


class item:
    def __init__(self):
        self.level = 1
        self.name = ""
        self.funcName = ""
        self.line = 0

    def __str__(self):
        return ("level=%s, name=%s, funcName=%s, line=%s\n" % (self.level, self.name, self.funcName, self.line))


def dict2List(inDict, level, retList):
    for key in inDict:
        i = item()
        i.level = level
        i.name = key.split(".")[0].encode("utf-8")
        if isinstance(inDict[key], dict):
            retList.append(i)
            dict2List(inDict[key], level+1, retList)

        else:
            i.funcName = inDict[key]
            i.level = 0
            retList.append(i)

    return retList


def main():
    file_name = raw_input(u"请输入tecs路径：" )
    file_name = unicode(file_name, "utf-8")
    retDict = collections.OrderedDict()
    scan_tcst_path(file_name, retDict)

    retList = []
    dict2List(retDict, 1, retList)
    for i in retList:
        print("%s, %s, %s, %s\n" % (i.level, i.name, i.funcName, i.line))


if __name__ == '__main__':
    main()