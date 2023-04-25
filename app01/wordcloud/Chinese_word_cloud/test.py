# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:42:14 2021

@author: Cynthia
"""

import time
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator  # , STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import jieba  # cutting Chinese sentences into words

while True:
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

    time.sleep(5)
