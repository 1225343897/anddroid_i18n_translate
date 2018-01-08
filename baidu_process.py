
import hashlib
import urllib
import random
import urllib.parse
import urllib.request
import json

def tran(zh):
    appid = '20171129000100917'
    secretKey = 'YRyNMNbyzYpjuiFUKJFE'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = zh
    fromLang = 'zh'
    toLang = 'en'
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf8"))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    #print(myurl)
    httpClient = urllib.request.urlopen('http://api.fanyi.baidu.com'+myurl)
    #print("***********")
    responseStr = httpClient.read();
    jsonObj = json.loads(responseStr)
    #print(jsonObj)
    return jsonObj["trans_result"][0]["dst"]
