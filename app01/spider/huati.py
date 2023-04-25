import urllib
from urllib.parse import quote
import requests
import pandas as pd
from lxml import etree


url='https://tophub.today/n/VaobJ98oAj'

headers={
    'Cookie':'SINAGLOBAL=6715754335225.932.1677423807936; '
                 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whj1DvwWAlRl9y1aHqZ2zf25JpX5KMhUgL'
                 '.FoMNShM0ehzpSoq2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0BNe05EeKqc; UOR=,,cn.bing.com; '
                 'webim_unReadCount=%7B%22time%22%3A1680960574140%2C%22dm_pub_total%22%3A12%2C%22chat_group_client%22'
                 '%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A54%2C%22msgbox%22%3A0%7D; '
                 'XSRF-TOKEN=cl5uH0O4F_2WmZtD8giqNedR; ALF=1683601958; SSOLoginState=1681009958; '
                 'SCF=AnarOzycV64B2eaAhzAkkpZ70Ka9GeAMm4bfUiNsDspS9yNR-WqPEicEsMWnQXmRFim_XZdpcYOAt062vi4VnHQ.; '
                 'SUB=_2A25JNl13DeRhGeFJ71US8CzNzTqIHXVqQsm_rDV8PUNbmtAGLVHZkW9Nf8XfH1o-wsjOXHxDjtafx0tjVD4-fC01; '
                 '_s_tentry=weibo.com; Apache=6312961435755.3.1681009965610; '
                 'ULV=1681009965630:29:10:1:6312961435755.3.1681009965610:1680953975502; ',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}

response = requests.get(url=url,headers=headers)
html = etree.HTML(response.text)


href = html.xpath('//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr/td[2]/a/@href')
title = html.xpath('//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr/td[2]/a/text()')
# print(title)

num = html.xpath('//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr/td[3]/text()')
# str_num = str(num).split()
# print(str_num)

rank = []
topic_href = []
topic_title = []
topic_num = []
for i in range(0,42):
    # print(title[i])
    rank.append(i)
    topic_title.append(title[i])
    key = urllib.parse.quote(title[i])
    th = 'https://s.weibo.com/weibo?q={}%23'.format(key)
    topic_href.append(th)
    topic_num.append(num[i])

taolun = []
read = []
for i in topic_num:
    str_i = str(i).split()
    taolun.append(str_i[0])
    read.append(str_i[1])
# print(title[41])
# print(topic_href)

# read_num = str(num).split(" ")
# print(read_num)

df={}
df['rank'] = rank
df['topic_href'] = topic_href
df['topic_title'] = topic_title
df['taolun'] = taolun
df['read'] = read
print(df)
dg = pd.DataFrame(df)
dg.to_csv(r"D:\A_Code\python\django\yue_2_3_2_大改版 - 副本\spider\csv\huati.csv")


