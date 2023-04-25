import time
import urllib
from urllib.parse import quote
import requests
import pandas as pd
from lxml import etree

keys = input("请输入想搜索的超话:")
key = urllib.parse.quote(keys)
start_url = 'https://s.weibo.com/topic?q={}&pagetype=topic&topic=1&Refer=weibo_topic'.format(key)
# https://s.weibo.com/topic?q=%E4%BA%8C%E5%8D%81%E5%A4%A7&pagetype=topic&topic=1&Refer=weibo_topic&page=2
print(start_url)
headers = {
    'Cookie': 'SINAGLOBAL=6715754335225.932.1677423807936; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whj1DvwWAlRl9y1aHqZ2zf25JpX5KMhUgL.FoMNShM0ehzpSoq2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0BNe05EeKqc; ALF=1683169318; SSOLoginState=1680577319; SCF=AnarOzycV64B2eaAhzAkkpZ70Ka9GeAMm4bfUiNsDspSJ_svLV-d1dDUuwWCvU9itjGL2Ykkj0Yu_CdmefLJCjY.; SUB=_2A25JL-N3DeRhGeFJ71US8CzNzTqIHXVqXVO_rDV8PUNbmtANLU7tkW9Nf8XfH2oeTFZfdsFw4iwGMz6P8ftZce6Y; _s_tentry=login.sina.com.cn; Apache=1410014674201.6494.1680577321035; ULV=1680577321065:22:3:3:1410014674201.6494.1680577321035:1680530914961',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}

def run_task():
    # 执行你想要定时运行的代码
    taolun = []
    read = []
    w_href = []
    w_title = []
    for i in range(1, 3):
        url = start_url + '&page={}'.format(i)
        print(url)
        response = requests.get(url=url, headers=headers)
        html = etree.HTML(response.text)

        href = html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div[1]/a/@href')
        # //*[@id="pl_feedlist_index"]/div[1]/div[1]/div[1]/a
        # //*[@id="pl_feedlist_index"]/div[1]/div[2]/div[1]/a
        print(href)

        title = html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div[2]/div/a/text()')
        # //*[@id="pl_feedlist_index"]/div[1]/div[1]/div[2]/div/a
        # //*[@id="pl_feedlist_index"]/div[1]/div[2]/div[2]/div/a
        print(title)

        for i in href:
            w_href.append(i)
        for i in title:
            w_title.append(i)

        num = html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div[2]/p[2]/text()')
        # //*[@id="pl_feedlist_index"]/div[1]/div[1]/div[2]/p[2]
        # //*[@id="pl_feedlist_index"]/div[1]/div[2]/div[2]/p[2]
        # print(num)
        content = html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div/div[2]/p[1]/text()')
        # //*[@id="pl_feedlist_index"]/div[1]/div[2]/div[2]/p[1]
        # //*[@id="pl_feedlist_index"]/div[1]/div[3]/div[2]/p[1]
        print(content)

        for i in num:
            str_i = str(i).split()
            taolun.append(str_i[0])
            read.append(str_i[1])
        print(taolun)
        print(read)
        content.insert(0, ' ')
    df = {}
    df['href'] = w_href
    df['标题'] = w_title
    df['讨论'] = taolun
    df['阅读'] = read
    print(df)
    dg = pd.DataFrame(df)
    dg.to_csv("{}.csv".format(keys))

    print('Task running at:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


# 设置时间间隔（以秒为单位）
interval = 10

# 获取当前时间戳
current_time = time.time()

# 计算下一次运行的时间戳
next_run_time = current_time + interval

while True:
    # 获取当前时间戳
    current_time = time.time()

    # 如果当前时间戳大于或等于下一次运行的时间戳，则运行任务
    if current_time >= next_run_time:
        run_task()
        # 计算下一次运行的时间戳
        next_run_time = current_time + interval
    else:
        # 否则，暂停程序
        time.sleep(1)