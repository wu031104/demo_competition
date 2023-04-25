import urllib
from urllib.parse import quote
import requests
import pandas as pd
from lxml import etree

keys = input("请输入想搜索的超话:")
key = urllib.parse.quote(keys)
url='https://s.weibo.com/topic?q={}&pagetype=topic&topic=1&Refer=weibo_topic'.format(key)

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

href = html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div[1]/a/@href')
# //*[@id="pl_feedlist_index"]/div[1]/div[1]/div[1]/a
# //*[@id="pl_feedlist_index"]/div[1]/div[2]/div[1]/a
print(href)

title = html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div[2]/div/a/text()')
# //*[@id="pl_feedlist_index"]/div[1]/div[1]/div[2]/div/a
# //*[@id="pl_feedlist_index"]/div[1]/div[2]/div[2]/div/a
print(title)

num = html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div[2]/p[2]/text()')
# //*[@id="pl_feedlist_index"]/div[1]/div[1]/div[2]/p[2]
# //*[@id="pl_feedlist_index"]/div[1]/div[2]/div[2]/p[2]
# print(num)

content = html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div[2]/p[1]/text()')
# //*[@id="pl_feedlist_index"]/div[1]/div[2]/div[2]/p[1]
# //*[@id="pl_feedlist_index"]/div[1]/div[3]/div[2]/p[1]
print(content)


taolun = []
read = []
for i in num:
    str_i = str(i).split()
    taolun.append(str_i[0])
    read.append(str_i[1])
print(taolun)
print(read)
content.insert(0,' ')
df={}
df['href'] = href
df['标题'] = title
df['讨论'] = taolun
df['阅读'] = read
print(df)
dg = pd.DataFrame(df)
dg.to_csv(r"D:\A_Code\python\django\yue_2_3_2_大改版 - 副本\spider\csv\{}topic.csv".format(keys))


