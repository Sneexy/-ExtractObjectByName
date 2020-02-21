#!/usr/bin/python
# -*- coding: UTF-8 -*-
from xml.dom.minidom import parse
import xml.dom.minidom 

def ExtractObjectByName(objcetNameList, inputFilename, outputFilename):
   
  # try: 打开文档容错用的，需要就替换下段第一句
  #     DOMTree = xml.dom.minidom.parse(inputFilename)
  # except FileNotFoundError:
  #     break
    
  # 使用minidom解析器打开 XML 文档
  DOMTree = xml.dom.minidom.parse(inputFilename)
  annotation = DOMTree.documentElement

  # 在集合中获取所有object
  objects = annotation.getElementsByTagName("object")

  # 删除名称不满足的
  for obj in objects:
    objectname = obj.getElementsByTagName("name")[0].childNodes[0].data
    if objectname not in mylist:
      annotation.removeChild(obj)

  with open(outputFilename, 'w') as fh:
    DOMTree.writexml(fh, encoding="utf-8-sig") #utf-8-sig可使输出中文不乱码
    
  print ("完成提取。")
  return
  
# ExtractObjectByName
mylist = ["a","a1"]
inputFilename = "input.xml" # 路径可以用绝对地址，路径中用双反斜杠\\
outputFilename = "output.xml"
ExtractObjectByName(mylist, inputFilename, outputFilename)