# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:42:14 2021

@author: Cynthia
"""

import numpy as np
from wordcloud import WordCloud, ImageColorGenerator#, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import jieba # cutting Chinese sentences into words

import pandas as pd
import requests
from lxml import etree
import time
import csv
import re


import pandas as pd
import requests
from lxml import etree
import time
import csv
import re

import stylecloud
def get_data():
    headers = {
        "cookie": 'SINAGLOBAL=6715754335225.932.1677423807936; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whj1DvwWAlRl9y1aHqZ2zf25JpX5KMhUgL.FoMNShM0ehzpSoq2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNS0BNe05EeKqc; ALF=1683169318; SSOLoginState=1680577319; SCF=AnarOzycV64B2eaAhzAkkpZ70Ka9GeAMm4bfUiNsDspSJ_svLV-d1dDUuwWCvU9itjGL2Ykkj0Yu_CdmefLJCjY.; SUB=_2A25JL-N3DeRhGeFJ71US8CzNzTqIHXVqXVO_rDV8PUNbmtANLU7tkW9Nf8XfH2oeTFZfdsFw4iwGMz6P8ftZce6Y; _s_tentry=login.sina.com.cn; Apache=1410014674201.6494.1680577321035; ULV=1680577321065:22:3:3:1410014674201.6494.1680577321035:1680530914961; UOR=,,www.bing.com',
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
        for month in range(3, 4):
            for day in range(12, 15):
                print(f'正在爬取{year}年{month}月{day}日')
                for page in range(1, 6):
                    print(f'正在爬取第{page}页')
                    if month < 10:
                        if day < 9:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-0{month}-0{day}-0:{year}-0{month}-0{day + 1}-0",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                        elif day == 9:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-0{month}-0{day}-0:{year}-0{month}-{day + 1}-0",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                        else:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-0{month}-{day}-0:{year}-0{month}-{day + 1}-0",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                    else:
                        if day < 9:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-{month}-0{day}-0:{year}-{month}-0{day + 1}-0",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                        elif day == 9:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-{month}-0{day}-0:{year}-{month}-{day + 1}-0",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                        else:
                            params = {
                                "q": keys,
                                "typeall": "1",
                                "suball": "1",
                                "timescope": f"custom:{year}-{month}-{day}-0:{year}-{month}-{day + 1}-0",
                                "Refer": "g",
                                "page": f"{page}"
                            }
                    while True:
                        try:
                            r = requests.get(url, headers=headers, params=params, timeout=5)
                            # https://s.weibo.com/weibo?q=任嘉伦&typeall=1&suball=1&timescope=custom:2022-10-1-0:2022-10-2-0&Refer=g&page=1
                            break
                        except:
                            print('网络链错误...')
                            time.sleep(2)
                    # print(r.text)
                    html = etree.HTML(r.text)
                    divs = html.xpath('.//div[@action-type="feed_list_item"]')
                    first_check = html.xpath('//div[@action-type="feed_list_item"]//div[@class="from"]/a[1]/text()')[
                        0].strip()
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
                        if zf[1] == ' 转发':
                            zf = 0
                        else:
                            zf = zf[1]
                        pl = div.xpath('.//div[@class="card-act"]/ul/li[2]/a/text()')
                        if pl[0] == ' 评论':
                            pl = 0
                        else:
                            pl = pl[0]
                        dz = div.xpath('.//div[@class="card-act"]/ul/li[3]//span[@class="woo-like-count"]/text()')
                        if dz[0] == '赞':
                            dz = 0
                        else:
                            dz = dz[0]
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
                        # print(times[0].strip(),'https:'+comment_url[0], nick_name[0], content_all,zf, pl, dz)
                        weibo_time.append(times[0].strip())
                        weibo_href.append('https:' + comment_url[0])
                        weibo_author.append(nick_name[0])
                        weibo_content.append(content_all)
                        weibo_share_num.append(zf)
                        weibo_pinglun_num.append(pl)
                        weibo_dianzan_num.append(dz)
                    #     with open(f'{file_name}.csv', 'a', encoding='utf-8', newline='') as f:
                    #         writer = csv.writer(f)
                    #         writer.writerow([times[0].strip(),'https:'+comment_url[0], nick_name[0], content_all,zf, pl, dz,uid[0]])
                    # time.sleep(1)

    # df = {}
    # df['times'] = weibo_time
    # df['href'] = weibo_href
    # df['author'] = weibo_author
    # df['content'] = weibo_content
    # df['share_num'] = weibo_share_num
    # df['pingllun_num'] = weibo_pinglun_num
    # df['dianzan_num'] = weibo_dianzan_num
    # print(df)
    # dg = pd.DataFrame(df)
    # dg.to_csv("search.txt")

    # f = open(r'D:\A_Code\python\django\yue_2_3_2_大改版 - 副本\app01\wordcloud\Chinese_word_cloud\texts\{}.txt'.format(keys), "w",
    #          encoding='utf-8')
    # f = open('{}.txt'.format(keys), "w",encoding='utf-8')
    f = open(r'D:\A_Code\python\django\yue_2_3_2_end\app01\wordcloud\Chinese_word_cloud\texts\{}.txt'.format(keys), "w",
             encoding='utf-8')
    for line in weibo_content:
        f.write(line)
        f.write('\n')


if __name__ == '__main__':
    keys = input("请输入想搜索的超话:")
    file_name = keys
    get_data()

# ----------------------------------------------------------------------------

def plt_imshow(x, ax=None, show=True):
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(x)
    ax.axis("off")
    if show: plt.show()
    return ax

def count_frequencies(word_list):
    freq = dict()
    for w in word_list:
        if w not in freq.keys():
            freq[w] = 1
        else:
            freq[w] += 1
    return freq


# In[]
if __name__ == '__main__':
    # setting paths
    fname_text = 'texts/{}.txt'.format(keys)
    fname_stop = 'stopwords/hit_stopwords.txt'
    fname_mask = 'pictures/img.png'
    fname_font = 'SourceHanSerifK-Light.otf'

    # read in texts (an article)
    text = open(fname_text, encoding='utf8').read()
    # Chinese stop words
    STOPWORDS_CH = open(fname_stop, encoding='utf8').read().split()

    # processing texts: cutting words, removing stop-words and single-charactors
    word_list = [
            w for w in jieba.cut(text)
            if w not in STOPWORDS_CH and len(w) > 1
            ]
    freq = count_frequencies(word_list)

    # processing image
    im_mask = np.array(Image.open(fname_mask))
    im_colors = ImageColorGenerator(im_mask)

    wcd = WordCloud(background_color='white', font_path=fname_font, height=400,
                          width=800, scale=20, prefer_horizontal=0.9999, max_words=800, max_font_size=80,
                          min_font_size=4, relative_scaling=0.3,
                          mask=im_mask
                          )
    # wcd.generate(text) # for English words
    # wcd.generate_from_frequencies(freq)
    # wcd.recolor(color_func = im_colors)
    #
    # # visualization
    # ax = plt_imshow(wcd,)
    # ax.figure.savefig(fr'D:\A_Code\python\django\yue_2_3_2_大改版 - 副本\app01\static\img_new\{keys}.png', bbox_inches='tight', dpi=150)
# ax.figure.savefig('{}.png'.format(keys), bbox_inches='tight', dpi=150)

    clouds = stylecloud.gen_stylecloud(
        text=freq,  # 上面分词的结果作为文本传给text参数
        size=512,
        font_path='C:/Windows/Fonts/msyh.ttc',  # 字体设置
        palette='cartocolors.qualitative.Pastel_7',  # 调色方案选取，从palettable里选择   colors.ListedColormap(['#FF0000', '#FF7F50', '#FFE4C4'])
        gradient='horizontal',  # 渐变色方向选了垂直方向
        icon_name='fab fa-weixin',  # 蒙版选取，从Font Awesome里选
        output_name=fr'D:\A_Code\python\django\yue_2_3_2_大改版 - 副本\app01\static\img_new\{keys}.png')  # 输出词云图
