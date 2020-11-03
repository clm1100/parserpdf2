import pdfplumber
import shutil
import re


def dealPDF1(p,content):
    matchObj = re.search(r'发票代码:[0-9]+', content, re.M | re.I)
    matchObj2 = re.search(r'发票号码:[0-9]+', content, re.M | re.I)
    matchObj3 = re.search(r'（小写）￥[0-9]+[.]?[0-9]+', content, re.M | re.I)
    code = matchObj.group().split(':')[1]
    num = matchObj2.group().split(':')[1]
    money = matchObj3.group().split('￥')[1]
    # print(code)
    # print(num)
    # print(money)
    dist ='./pdf2/'+code+'-'+num+'-'+money+'-'+'陈黎明'+'.pdf'
    shutil.copyfile(p, dist)
