# anddroid_i18n_translate
android国际化，翻译strings.xml
其中tran_baidu.py是程序的开始入口

需要修改的地方：
#1、tran_baidu.py中的domTree = xml.dom.minidom.parse("../xml/strings2.xml")的实际路径
#2、tran_baidu.py中的domTree.writexml(open("../xml/en.xml","w",encoding="utf8"),addindent = '' , newl = '' ,encoding = 'utf-8' )根据实际情况进行修改
