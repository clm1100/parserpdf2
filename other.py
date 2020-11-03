import pdfplumber
import shutil
import re

def dealPDF2(p): 
    with pdfplumber.open(p) as pdf:
        page= pdf.pages[0]
        content = page.extract_text()
        # print(content)
        print(content.find('电子报销凭证序号'))
        matchObj = re.search(r'电子报销凭证序号 [0-9]+', content, re.M | re.I)
        matchObj2 = re.search(r'费用合计：CNY[0-9]+[.]?[0-9]+', content, re.M | re.I)
        code = matchObj.group().split(' ')[1]
        money = matchObj2.group().split('CNY')[1]
        print(code)
        print(money)
        dist = code+'-'+money+'-'+'陈黎明'+'.pdf'
        shutil.copyfile(p, dist)

