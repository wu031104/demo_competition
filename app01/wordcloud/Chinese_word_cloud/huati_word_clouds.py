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

import requests

from lxml import etree

import time

import stylecloud





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
    fname_text = 'texts/huati_2.txt'
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
    clouds = stylecloud.gen_stylecloud(
        text=freq,  # 上面分词的结果作为文本传给text参数
        size=512,
        font_path='C:/Windows/Fonts/msyh.ttc',  # 字体设置
        palette='cartocolors.qualitative.Pastel_7',  # 调色方案选取，从palettable里选择
        gradient='horizontal',  # 渐变色方向选了垂直方向
        icon_name='fab fa-weixin',  # 蒙版选取，从Font Awesome里选
        output_name=fr'D:\A_Code\python\django\yue_2_3_2_end\app01\static\img_new\huati_word_clouds.png')  # 输出词云图

