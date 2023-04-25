import time


def run_task():
    # 执行你想要定时运行的代码
    import re
    import requests
    import pandas as pd
    from lxml import etree

    url = 'https://s.weibo.com/top/summary?cate=realtimebot'

    headers = {
        'Cookie': 'SINAGLOBAL=5144919636304.006.1679922733568; '
                  'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWk95cTkYho18H.ST-4XUow5JpX5KMhUgL'
                  '.FoMNSKBEeKqfSh22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0-Xeo2cSKBp; UOR=,,login.sina.com.cn; '
                  'WBPSESS=R2i4HySPkgY21zd3TMf6n9uMvmdsvh5Fbowo70YOThYVCA98J9mwUP604mOGXkW_HC_hxgl7'
                  '-4bEZ_M2n21x9ldR2HMgHEwQ5wCCfjM5tRvJ61KMgd4il_1lMQ1oF0zT1nt8bBH__Vn8JVQ9H9A1jA==; '
                  'XSRF-TOKEN=ItAh-iCbFjmfeQM6__S2llhz; ALF=1683120736; SSOLoginState=1680528737; '
                  'SCF=AuacW-PP-C6hHuVXOoQogp5ZeCIsfnSdO3TebmiFodgWOt7wPTKi84ikMAS_lfO5VDEHZq9mKOxX9nmDeXawmKQ.; '
                  'SUB=_2A25JLqUyDeRhGeFJ7lYT8SjJzz2IHXVqXZH6rDV8PUNbmtANLRPBkW9Nf7z7oyZUhBff2P-P-MhLXIhj4wnqmEnF; '
                  '_s_tentry=weibo.com; Apache=4127855143957.5283.1680528772445; '
                  'ULV=1680528772459:7:3:3:4127855143957.5283.1680528772445:1680506068127; '
                  'UPSTREAM-V-WEIBO-COM=35846f552801987f8c1e8f7cec0e2230',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
    }

    response = requests.get(url=url, headers=headers)
    html = etree.HTML(response.text)

    title = html.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]/a/text()')
    # //*[@id="pl_top_realtimehot"]/table/tbody/tr[1]/td[2]/a
    # //*[@id="pl_top_realtimehot"]/table/tbody/tr[2]/td[2]/a
    # //*[@id="pl_top_realtimehot"]/table/tbody/tr[4]/td[2]/a
    print(title)

    f = open('hot1.txt', "w", encoding='utf-8')
    for line in title:
        f.write(line)
        f.write('\n')
    print('Task running at:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


# 设置时间间隔（以秒为单位）
interval = 60

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