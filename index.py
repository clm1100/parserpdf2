from one import dealPDF1
from other import dealPDF2
import os
import pdfplumber
file_list = os.listdir('./pdf')
for fname in file_list:
    if '.pdf' in fname:
        # print(fname)
        p = './pdf/'+fname
        with pdfplumber.open(p) as pdf:
            page = pdf.pages[0]
            content = page.extract_text()
            print('===============')
            print(p)
            print(content)
            print('===============')
            # if content.find('电子报销凭证序号') > 0:
            #     print(fname)
            #     dealPDF2(p,content)
            # else:
            #     dealPDF1(p,content)


