import re
import requests
import pandas as pd
from lxml import etree


import time


while True:
    url='https://s.weibo.com/top/summary?cate=realtimebot'

    headers={
        'Cookie':'SINAGLOBAL=5144919636304.006.1679922733568; UOR=,,login.sina.com.cn; '
              'ULV=1680528772459:7:3:3:4127855143957.5283.1680528772445:1680506068127; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWk95cTkYho18H.ST-4XUow5JpX5KMhUgL'
              '.FoMNSKBEeKqfSh22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0-Xeo2cSKBp; XSRF-TOKEN=1G58g2D12zNA0YE6-rLVVHYZ; '
              'ALF=1683994304; SSOLoginState=1681402305; '
              'SCF=AuacW-PP-C6hHuVXOoQogp5ZeCIsfnSdO3TebmiFodgW0rMcvYR_zc_5DBAGsTCro40I5fUKD1Wfb99mW4r83y0.; '
              'SUB=_2A25JPFmSDeRhGeFJ7lYT8SjJzz2IHXVqSMxarDV8PUNbmtAbLUT-kW9Nf7z7o2xzI8YPEbEabtHoZ5Ietn8TERCA; '
              'WBPSESS=R2i4HySPkgY21zd3TMf6n9uMvmdsvh5Fbowo70YOThYVCA98J9mwUP604mOGXkW_HC_hxgl7'
              '-4bEZ_M2n21x9tUKCbWeNReatJzORFfZRquCe5CXd8F43g3m_toJMmqL3A26sZFrtQ3VQzd0Gd-VEQ==',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
    }

    response = requests.get(url=url,headers=headers)
    html = etree.HTML(response.text)

    title = html.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]/a/text()')
    # //*[@id="pl_top_realtimehot"]/table/tbody/tr[1]/td[2]/a
    # //*[@id="pl_top_realtimehot"]/table/tbody/tr[2]/td[2]/a
    # //*[@id="pl_top_realtimehot"]/table/tbody/tr[4]/td[2]/a
    print(title)

    f=open(r'D:\A_Code\python\django\yue_2_3_2_大改版 - 副本\app01\wordcloud\Chinese_word_cloud\texts\hot_2.txt', "w", encoding='utf-8')
    for line in title:
        f.write(line)
        f.write('\n')

    time.sleep(5)