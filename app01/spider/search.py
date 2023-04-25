import pandas as pd
import requests
from lxml import etree
import time
import csv
import re


def get_data():
    headers = {
        "cookie":'SINAGLOBAL=5144919636304.006.1679922733568; UOR=,,login.sina.com.cn; '
                 'XSRF-TOKEN=ItAh-iCbFjmfeQM6__S2llhz; SSOLoginState=1680528737; _s_tentry=weibo.com; '
                 'Apache=4127855143957.5283.1680528772445; '
                 'ULV=1680528772459:7:3:3:4127855143957.5283.1680528772445:1680506068127; '
                 'UPSTREAM-V-WEIBO-COM=35846f552801987f8c1e8f7cec0e2230; '
                 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWk95cTkYho18H.ST-4XUow5JpX5KMhUgL'
                 '.FoMNSKBEeKqfSh22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0-Xeo2cSKBp; ALF=1683806157; '
                 'SCF=AuacW-PP-C6hHuVXOoQogp5ZeCIsfnSdO3TebmiFodgWBc9s7OzBhrDCSZADx4i_9Y8i6A1SY8ApLB3ka1Dy4UI.; '
                 'SUB=_2A25JMTqADeRhGeFJ7lYT8SjJzz2IHXVqRytIrDV8PUNbmtAbLVP3kW9Nf7z7owBBCDDemZlcqbFe_6-tr-3DqBQO; '
                 'WBPSESS=R2i4HySPkgY21zd3TMf6n9uMvmdsvh5Fbowo70YOThYVCA98J9mwUP604mOGXkW_HC_hxgl7'
                 '-4bEZ_M2n21x9iqu7tED0YOqtK808B4Ym8NAGys60R-KlGu02SRVK9IwDnurJmIzkazuF52UzDapYA==',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56"
    }
    url = "https://s.weibo.com/weibo"
    weibo_time = []
    weibo_href = []
    weibo_author = []
    weibo_content = []
    weibo_share_num = []
    weibo_pinglun_num = []
    weibo_dianzan_num = []
    for year in range(2023, 2024):
        for month in range(4, 5):
            for day in range(1, 9):
                print(f'正在爬取{year}年{month}月{day}日')
                for page in range(1,51):
                    print(f'正在爬取第{page}页')
                    if month < 10:
                        if day < 9:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-0{month}-0{day}-0:{year}-0{month}-0{day}-23",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                        elif day == 9:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-0{month}-0{day}-0:{year}-0{month}-{day}-23",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                        else:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-0{month}-{day}-0:{year}-0{month}-{day}-23",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                    else:
                        if day < 9:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-{month}-0{day}-0:{year}-{month}-0{day}-23",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                        elif day == 9:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-{month}-0{day}-0:{year}-{month}-{day}-23",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                        else:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-{month}-{day}-0:{year}-{month}-{day}-23",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                    while True:
                        try:
                            r = requests.get(url, headers=headers, params=params, timeout=5)
                            # https://s.weibo.com/weibo?q=任嘉伦&typeall=1&suball=1&timescope=custom:2022-10-1-0:2022-10-2-0&Refer=g&page=1
                            # https://s.weibo.com/weibo?q=两会&typeall=1&suball=1&timescope=custom%3A2023-04-01-0%3A2023-04-09-23&Refer=g&page=1
                            break
                        except:
                            print('网络链错误...')
                            time.sleep(2)
                    # print(r.text)
                    html = etree.HTML(r.text)
                    divs = html.xpath('.//div[@action-type="feed_list_item"]')
                    first_check = html.xpath('//div[@action-type="feed_list_item"]//div[@class="from"]/a[1]/text()')[0].strip()
                    if not first_check.count('月'):
                        print('无当日内容 已跳出.')
                        break
                    if not divs:
                        print('无内容,跳出循环')
                        break
                    for div in divs:
                        # 用户名和uid
                        nick_name = div.xpath('.//div[@class="content"]/div[@class="info"]/div[2]/a/@nick-name')
                        href = div.xpath('.//div[@class="content"]/div[@class="info"]/div[2]/a/@href')
                        uid = re.findall('//weibo.com/(.*?)\?refer_flag', href[0], re.S)
                        times = div.xpath('.//div[@class="from"]/a[1]/text()')  # 发布时间
                        comment_url = div.xpath('.//div[@class="from"]/a/@href')  # 正文主页
                        # print(comment_url)
                        # 转发点赞评论数量
                        zf = div.xpath('.//div[@class="card-act"]/ul/li[1]/a/text()')
                        if zf[1]==' 转发':
                            zf=0
                        else:
                            zf=zf[1]
                        pl = div.xpath('.//div[@class="card-act"]/ul/li[2]/a/text()')
                        if pl[0]==' 评论':
                            pl=0
                        else:
                            pl=pl[0]
                        dz = div.xpath('.//div[@class="card-act"]/ul/li[3]//span[@class="woo-like-count"]/text()')
                        if dz[0]=='赞':
                            dz=0
                        else:
                            dz=dz[0]
                        # print(zf, pl, dz)
                        # 发布内容
                        contents = div.xpath('.//p[@node-type="feed_list_content"]//text()')
                        contents_zk = div.xpath('.//p[@node-type="feed_list_content_full"]//text()')
                        content_all = ''
                        if contents and not contents_zk:
                            for co in contents:
                                content_all += co.strip().replace('展开', '')
                        elif contents and contents_zk:
                            for co in contents_zk:
                                content_all += co.strip()
                        comment_id = div.xpath('.//@mid')  # 评论id
                        # print(href)
                        print(times[0].strip(),'https:'+comment_url[0], nick_name[0], content_all,zf, pl, dz)
                        weibo_time.append(times[0].strip())
                        weibo_href.append('https:'+comment_url[0])
                        weibo_author.append(nick_name[0])
                        weibo_content.append(content_all)
                        weibo_share_num.append(zf)
                        weibo_pinglun_num.append(pl)
                        weibo_dianzan_num.append(dz)
                    #     with open(f'{file_name}.csv', 'a', encoding='utf-8', newline='') as f:
                    #         writer = csv.writer(f)
                    #         writer.writerow([times[0].strip(),'https:'+comment_url[0], nick_name[0], content_all,zf, pl, dz,uid[0]])
                    # time.sleep(1)

    df = {}
    df['times'] = weibo_time
    df['herf'] = weibo_href
    df['author'] = weibo_author
    df['content'] = weibo_content
    df['share_num'] = weibo_share_num
    df['pingllun_num'] = weibo_pinglun_num
    df['dianzan_num'] = weibo_dianzan_num
    print(df)
    dg = pd.DataFrame(df)
    dg.to_csv(r"D:\A_Code\python\django\yue_2_3_2_大改版 - 副本\app01\spider\csv\{}.search.csv".format(keys))
    # dg.to_csv("search.csv")


if __name__ == '__main__':
    keys = input("请输入想搜索的超话:")
    file_name = keys
    get_data()
