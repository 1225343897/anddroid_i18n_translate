import xml.dom.minidom
from xml.dom.minidom import parse

from 国际化翻译.baidu_process import tran


def process_domTree(domTree):
   collection = domTree.documentElement
   strs = collection.getElementsByTagName("string")
   for str in strs:
      orgStr = str.childNodes[0].data;
      tranStr = tran(orgStr);
      str.childNodes[0].data = tranStr;
      print(orgStr,"---->",tranStr)

domTree = xml.dom.minidom.parse("../xml/strings2.xml")
process_domTree(domTree)
domTree.writexml(open("../xml/en.xml","w",encoding="utf8"),addindent = '' , newl = '' ,encoding = 'utf-8' )
