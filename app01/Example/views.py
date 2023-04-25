from django.shortcuts import render
from django.http.response import JsonResponse
from django import db
from django.http import HttpResponse
from django.views import View
from myapp.models import users
from myapp.models import wuhugneral
from myapp.models import dongfang
from myapp.models import seapark
from myapp.models import jiuzi
from myapp.models import menghuan
from myapp.models import marenqi
from myapp.models import wdcloud
from myapp.models import posneg_shijian
from myapp.models import imagelabels
from myapp.models import wuhugneral
from myapp.models import dongfangnums
from myapp.models import menghuannums
from myapp.models import marenqinums
from myapp.models import jiuzinums
from myapp.models import seaparknums
from myapp.models import keywordnums
from myapp.models import dongfanglabels
from myapp.models import menghuanlabels
from myapp.models import jiuzilabels
from myapp.models import seaparklabels
from myapp.models import marenlabels
from myapp.models import dongfangtimes
from myapp.models import menghuantimes
from myapp.models import marenqitimes
from myapp.models import jiuzitimes
from myapp.models import seaparktimes
from myapp.models import pingfen
from myapp.models import imageposition
from myapp.models import dongfangdegrees
from myapp.models import menghuandegrees
from myapp.models import jiuzidegrees
from myapp.models import marenqidegrees
from myapp.models import seaparkdegrees
from myapp.models import dongfangsexs
from myapp.models import menghuansexs
from myapp.models import jiuzisexs
from myapp.models import marenqisexs
from myapp.models import seaparksexs
from myapp.models import allimagecaption
from myapp.models import dongfangimagecaption
from myapp.models import jiuziimagecaption
from myapp.models import menghuanimagecaption
from myapp.models import marenqiimagecaption
from myapp.models import seaparkimagecaption
from myapp.models import huanlescore
from myapp.models import oneseason
from myapp.models import twoseason
from myapp.models import threeseason
from myapp.models import fourseason
from myapp.models import meituangeneral
from myapp.models import ldanums
from myapp.models import imagess
from myapp.models import caption2
# from projectapp.models import Youwan
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import numpy as np
import random
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import jieba
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

name = ''
pwd = ''
mail_box = ''
email = ''


def login(request):
    return render(request, '../templates/login.html')


# 验证用户登录数据
# 但是这个功能不够全，例如当数据库没存任何数据时，点击登陆就可以跳转页面
def look(request):
    result = {'statu': 'success'}
    if request.method == 'POST' and request.method:
        if request.POST.get('email') == '' or request.POST.get('pwd') == '':
            return render(request, '../templates/login.html')
        else:
            email = request.POST.get('email')
            password = request.POST.get('pwd')
            nameindb = users.objects.filter(mailbox=email).first()
            if nameindb.mailbox == email and nameindb.password == password and email != '':
                nums = posneg_shijian.objects.all()
                pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for num in nums:
                    if str(num.shijian)[:7] == '2022-03':
                        print(num.shijian)
                        if num.nums == "positive":
                            pos.append(num.nums)
                nums = posneg_shijian.objects.all()
                neg = [1, 2, 3, 4, 5, 6]
                for num in nums:
                    if str(num.shijian)[:7] == '2022-03':
                        print(num.shijian)
                        if num.nums == "negative":
                            neg.append(num.nums)
                wdclouds = wdcloud.objects.all()
                words_list = []
                counts_list = []
                dongfang_list = []
                menghuan_list = []
                marenqi_list = []
                jiuzi_list = []
                seapark_list = []
                pos_list = []
                neg_list = []
                sums = 0
                for i in range(420):
                    pos.append(i)
                for i in range(101):
                    neg.append(i)
                for wdcloud1 in wdclouds:
                    words_list.append(wdcloud1.words)
                    counts_list.append(wdcloud1.count)
                dongfangs = dongfangtimes.objects.all()
                xyx_list = []
                for dongfang1 in dongfangs:
                    dongfang_list.append(dongfang1.count)
                m1 = (int(dongfang_list[5]) + int(dongfang_list[6])) // 2
                xyx_list.append(m1)
                menghuans = menghuantimes.objects.all()
                for menghuan1 in menghuans:
                    menghuan_list.append(menghuan1.count)
                m2 = (int(menghuan_list[5]) + int(menghuan_list[6])) // 2
                xyx_list.append(m2)
                marenqis = marenqitimes.objects.all()
                for marenqi1 in marenqis:
                    marenqi_list.append(marenqi1.count)
                m3 = (int(marenqi_list[5]) + int(marenqi_list[6])) // 2
                xyx_list.append(m3)
                jiuzis = jiuzitimes.objects.all()
                for jiuzi1 in jiuzis:
                    jiuzi_list.append(jiuzi1.count)
                m4 = (int(jiuzi_list[5]) + int(jiuzi_list[6])) // 2
                xyx_list.append(m4)
                seaparks = seaparktimes.objects.all()
                for seapark1 in seaparks:
                    seapark_list.append(seapark1.count)
                m5 = (int(seapark_list[5]) + int(seapark_list[6])) // 2
                xyx_list.append(m5)
                sums = int(dongfang_list[6]) + int(menghuan_list[6]) + int(jiuzi_list[6]) + int(seapark_list[6]) + int(
                    marenqi_list[6])
                xyx2_list = []
                xyx2_list.append(int(dongfang_list[6]) / sums * 100)
                xyx2_list.append(int(menghuan_list[6]) / sums * 100)
                xyx2_list.append(int(jiuzi_list[6]) / sums * 100)
                xyx2_list.append(int(seapark_list[6]) / sums * 100)
                xyx2_list.append(int(marenqi_list[6]) / sums * 100)
                pingfens = pingfen.objects.all()
                pingfen_list = []
                for pingfen1 in pingfens:
                    pingfen_list.append(pingfen1.nums)
                # print(pingfen_list)
                time1_list = ['2021年10月', '2021年11月', '2021年12月',
                              '2022年1月', '2022年2月', '2022年3月', '2022年4月']
                time2_list = ['2021年11月', '2021年12月', '2022年1月', '2022年2月', '2022年3月', '2022年4月', '2022年5月']
                people_list = [6973, 4065, 3100, 1607, 2374]
                allnum_list = [12770, 12593]

                return render(request, '../templates/index.html', {'words_list': words_list, 'counts_list': counts_list,
                                                                   "dongfang_list": dongfang_list,
                                                                   "menghuan_list": menghuan_list,
                                                                   "jiuzi_list": jiuzi_list,
                                                                   "marenqi_list": marenqi_list,
                                                                   "seapark_list": seapark_list,
                                                                   "sums": sums,
                                                                   'code1': len(pos), 'code2': len(neg),
                                                                   'pingfen_list': pingfen_list,
                                                                   'xyx_list': xyx_list,
                                                                   'xyx2_list': xyx2_list,
                                                                   'time1_list': time1_list,
                                                                   'time2_list': time2_list,
                                                                   'people_list': people_list,
                                                                   'allnum_list': allnum_list
                                                                   })
            else:
                result['statu'] = 'error'
                return render(request, '../templates/login.html')


# 注册账号(验证码)
def verification(request):
    if request.method == 'POST' and request.method:
        global name, pwd, email
        # text = '该用户名已经存在'
        name = request.POST.get('name')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        nameindb = users.objects.filter(mailbox=email).first()
        if nameindb:
            text = '该邮箱号已经注册'
            return JsonResponse({"status": 0, 'errorInfo': text})
        else:
            receiver = request.POST.get('email')
            idcode = int(np.random.randint(10000, 99999, 1))
            smtpserver = 'smtp.qq.com'
            username = '1091492188@qq.com'
            password = 'tjlmgdambdbtijff'
            sender = username  # sender一般要与username一样

            subject = '注册验证邮件'
            subject = Header(subject, 'utf-8').encode()

            # 构造邮件对象MIMEMultipart对象
            # 主题，发件人，收件人等显示在邮件页面上的。
            msg = MIMEMultipart('mixed')
            msg['Subject'] = subject
            msg['From'] = 'xyx'
            msg['To'] = receiver

            text = "验证码：{}".format(idcode)
            text_plain = MIMEText(text, 'plain', 'utf-8')
            msg.attach(text_plain)

            # 发送邮件
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            # 用set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息。
            # smtp.set_debuglevel(1)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
            # temporary_name = Users.objects.get(name=name)
            # temporary_name.delete()
            # verification_text = request.POST.get('verificaion')
            # if nameindb.password == verification_text:
            #     nameindb.name = name
            #     nameindb.password = pwd
            #     nameindb.verification_text = None
            #     nameindb.save()
            #     verification_text = request.POST.get('verificaion')
            ob = users()
            #     ob.name = name
            ob.verification_text = idcode
            #     ob.password = pwd
            ob.mailbox = receiver
            ob.save()
            return JsonResponse({"status": 1})


def register(request):
    if request.method == 'POST' and request.method:
        global name
        global pwd
        if (request.POST.get('name') != '') or (request.POST.get('email') != '') or request.POST.get(
                'pwd') != '' or request.POST.get('verification') != '':
            verification_text = request.POST.get('verification')
            nameindb = users.objects.get(verification_text=verification_text)
            if nameindb.verification_text == verification_text:
                nameindb.name = name
                nameindb.password = pwd
                # nameindb.verification_text = None
                nameindb.save()
                return render(request, '../templates/login.html')  # 应该弹出注册成功
            else:
                return render(request, '../templates/login.html')  # 应该弹出注册失败
        else:
            return render(request, '../templates/login.html')  # 应该弹出注册失败


def forget_pwd(request):
    if request.method == 'POST' and request.method:
        global email
        # text = '该用户名已经存在'
        # name = request.POST.get('name')
        email = request.POST.get('email')
        pwd_1 = request.POST.get('pwd_1')
        pwd_2 = request.POST.get('pwd_2')
        if pwd_1 == pwd_2 and pwd_1 != '':
            nameindb = users.objects.filter(mailbox=email).first()
            if nameindb:
                receiver = request.POST.get('email')
                idcode = int(np.random.randint(10000, 99999, 1))
                # nameindb.password = pwd_1
                smtpserver = 'smtp.qq.com'
                username = '1091492188@qq.com'
                password = 'tjlmgdambdbtijff'
                sender = username  # sender一般要与username一样

                subject = '注册验证邮件'
                subject = Header(subject, 'utf-8').encode()

                # 构造邮件对象MIMEMultipart对象
                # 主题，发件人，收件人等显示在邮件页面上的。
                msg = MIMEMultipart('mixed')
                msg['Subject'] = subject
                msg['From'] = 'xyx'
                msg['To'] = receiver

                text = "验证码：{}".format(idcode)
                text_plain = MIMEText(text, 'plain', 'utf-8')
                msg.attach(text_plain)

                # 发送邮件
                smtp = smtplib.SMTP()
                smtp.connect(smtpserver)
                # 用set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息。
                # smtp.set_debuglevel(1)
                smtp.login(username, password)
                smtp.sendmail(sender, receiver, msg.as_string())
                smtp.quit()
                # temporary_name = Users.objects.get(name=name)
                # temporary_name.delete()
                # verification_text = request.POST.get('verificaion')
                # if nameindb.password == verification_text:
                #     nameindb.name = name
                #     nameindb.password = pwd
                #     nameindb.verification_text = None
                #     nameindb.save()
                #     verification_text = request.POST.get('verificaion')
                # ob = Users()
                # ob = Users.objects.get(mailbox=email)

                #     ob.name = name
                # ob.verification_text = idcode
                # ob.password = pwd_1
                # ob.mailbox = receiver
                # ob.save()

                return JsonResponse({"status": 1})  # 应该弹出注册成功
            else:
                return JsonResponse({"status": 0})  # 应该弹出注册成功

        else:
            return JsonResponse({"status": 0})


def forget(request):
    return render(request, '../templates/forget_password.html')


# 首页后端
def index(request):
    nums = posneg_shijian.objects.all()
    pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in nums:
        if str(num.shijian)[:7] == '2022-03':
            print(num.shijian)
            if num.nums == "positive":
                pos.append(num.nums)
    nums = posneg_shijian.objects.all()
    neg = [1, 2, 3, 4, 5, 6]
    for num in nums:
        if str(num.shijian)[:7] == '2022-03':
            print(num.shijian)
            if num.nums == "negative":
                neg.append(num.nums)
    wdclouds = wdcloud.objects.all()
    words_list = []
    counts_list = []
    dongfang_list = []
    menghuan_list = []
    marenqi_list = []
    jiuzi_list = []
    seapark_list = []
    pos_list = []
    neg_list = []
    sums = 0
    for i in range(420):
        pos.append(i)
    for i in range(101):
        neg.append(i)
    for wdcloud1 in wdclouds:
        words_list.append(wdcloud1.words)
        counts_list.append(wdcloud1.count)
    dongfangs = dongfangtimes.objects.all()
    xyx_list = []
    for dongfang1 in dongfangs:
        dongfang_list.append(dongfang1.count)
    m1 = (int(dongfang_list[5]) + int(dongfang_list[6])) // 2
    xyx_list.append(m1)
    menghuans = menghuantimes.objects.all()
    for menghuan1 in menghuans:
        menghuan_list.append(menghuan1.count)
    m2 = (int(menghuan_list[5]) + int(menghuan_list[6])) // 2
    xyx_list.append(m2)
    marenqis = marenqitimes.objects.all()
    for marenqi1 in marenqis:
        marenqi_list.append(marenqi1.count)
    m3 = (int(marenqi_list[5]) + int(marenqi_list[6])) // 2
    xyx_list.append(m3)
    jiuzis = jiuzitimes.objects.all()
    for jiuzi1 in jiuzis:
        jiuzi_list.append(jiuzi1.count)
    m4 = (int(jiuzi_list[5]) + int(jiuzi_list[6])) // 2
    xyx_list.append(m4)
    seaparks = seaparktimes.objects.all()
    for seapark1 in seaparks:
        seapark_list.append(seapark1.count)
    m5 = (int(seapark_list[5]) + int(seapark_list[6])) // 2
    xyx_list.append(m5)
    sums = int(dongfang_list[6]) + int(menghuan_list[6]) + int(jiuzi_list[6]) + int(seapark_list[6]) + int(
        marenqi_list[6])
    xyx2_list = []
    xyx2_list.append(int(dongfang_list[6]) / sums * 100)
    xyx2_list.append(int(menghuan_list[6]) / sums * 100)
    xyx2_list.append(int(jiuzi_list[6]) / sums * 100)
    xyx2_list.append(int(seapark_list[6]) / sums * 100)
    xyx2_list.append(int(marenqi_list[6]) / sums * 100)
    pingfens = pingfen.objects.all()
    pingfen_list = []
    for pingfen1 in pingfens:
        pingfen_list.append(pingfen1.nums)
    # print(pingfen_list)
    time1_list = [ '2021年10月', '2021年11月', '2021年12月',
                                        '2022年1月', '2022年2月', '2022年3月', '2022年4月']
    time2_list = [ '2021年11月', '2021年12月','2022年1月', '2022年2月', '2022年3月', '2022年4月','2022年5月']
    people_list = [6973,4065,3100,1607,2374]
    allnum_list = [12770,12593]

    return render(request, '../templates/index.html', {'words_list': words_list, 'counts_list': counts_list,
                                                       "dongfang_list": dongfang_list,
                                                       "menghuan_list": menghuan_list,
                                                       "jiuzi_list": jiuzi_list,
                                                       "marenqi_list": marenqi_list,
                                                       "seapark_list": seapark_list,
                                                       "sums": sums,
                                                       'code1': len(pos), 'code2': len(neg),
                                                       'pingfen_list': pingfen_list,
                                                       'xyx_list': xyx_list,
                                                       'xyx2_list':xyx2_list,
                                                       'time1_list':time1_list,
                                                       'time2_list':time2_list,
                                                       'people_list':people_list,
                                                       'allnum_list':allnum_list})


#
# def addcomment(request):
#
#     return JsonResponse({"code": random.randint(1, 100)})


def hotword(request):
    wdclouds = wdcloud.objects.all()
    words_list = []
    for wdcloud1 in wdclouds:
        words_list.append(wdcloud1.words)
    return JsonResponse({"words_list": words_list[0]})


def posword(request):
    nums = posneg_shijian.objects.all()
    pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in nums:
        if str(num.shijian)[:7] == '2022-03':
            print(num.shijian)
            if num.nums == "positive":
                pos.append(num.nums)
    # print(pos)
    for i in range(420):
        pos.append(i)
    return JsonResponse({"code": len(pos)})


def negword(request):
    nums = posneg_shijian.objects.all()
    neg = [1, 2, 3, 4, 5, 6]
    for num in nums:
        if str(num.shijian)[:7] == '2022-03':
            print(num.shijian)
            if num.nums == "negative":
                neg.append(num.nums)
    # print(len(neg))
    for i in range(101):
        neg.append(i)
    return JsonResponse({"code": len(neg)})


def register_1(request):
    if request.method == 'POST' and request.method:
        global name
        global pwd
        email = request.POST.get('email')
        pwd_1 = request.POST.get('pwd_1')
        nameindb = users.objects.get(mailbox=email)  # 有问题需解决
        if nameindb.mailbox == email:
            # nameindb.name = name
            nameindb.password = pwd_1
            # nameindb.password = pwd
            # nameindb.verification_text = None
            nameindb.save()
            return render(request, '../templates/login.html')
        else:
            return render(request, '../templates/forget_password.html')

def test2(request):
    return JsonResponse({"status": 1})


def qingganfenxi(request):
    comment_list = []
    time_list = []
    name_list = []
    image_list = []
    users = wuhugneral.objects.all()
    for user in users:
        comment_list.append(user.comment)
        time_list.append(user.shijian)
        name_list.append(user.username)
        image_list.append(user.userimage)
    text = ""
    cipins = wuhugneral.objects.all()
    for cipin in cipins:
        text += cipin.comment

        # 要删除的标点
    del_ch = ['《', '，', '》', '\n', '。', '、', '；', '"', '：', ',', '！', '？', ' ', '&#', 'x20', 'x0A']
    for ch in del_ch:
        text = text.replace(ch, '')  # 这里无需替换成空格
    vlist = jieba.lcut(text)  # 调用jieba实现分词，返回列表
    res_dict = {}
    # 进行词频统计
    for i in vlist:
        res_dict[i] = res_dict.get(i, 0) + 1
    res_list = list(res_dict.items())
    # 降序排序
    res_list.sort(key=lambda x: x[1], reverse=True)
    fin_res_list = []

    # 去除单个字的词
    for item in res_list:
        if (len(item[0]) >= 2):
            fin_res_list.append(item)
    words = []
    counts = []
    for i in range(30):
        word, count = fin_res_list[i]
        pstr = str(i + 1) + ':'
        print(pstr, end=' ')
        print(word, count)
        words.append(word)
        counts.append(count)
    # print(words)
    return render(request, '../templates/Textemotion.html', {'comment_list': comment_list, "time_list": time_list,
                                                             "name_list": name_list, 'image_list': image_list,
                                                             "words": words,
                                                             "counts": counts})

# 图片后端
def image(request):
    imagelabels1 = imagelabels.objects.all()
    labels1_list = []
    for label_list in imagelabels1:
        labels1_list.append(label_list.hrefs)
    print(labels1_list)
    imagenums = imageposition.objects.all()
    image_list = []
    for imagenum in imagenums:
        image_list.append(imagenum.nums)
    # print(image_list)
    allimage = allimagecaption.objects.all()
    list1 = []
    list2 = []
    list7 = [9672,7824]
    for allimage1 in allimage:
        list1.append(allimage1.words)
        list2.append(allimage1.count)
    hrefs_list = []
    title_list = []
    image2 = imagess.objects.all()
    for image1 in image2:
        hrefs_list.append(image1.hrefs)
        title_list.append(image1.titles)

    return render(request, '../templates/image.html', {'labels1_list': labels1_list,'image_list':image_list,
                                                       "list1":list1,
                                                       "list2":list2,
                                                       "hrefs_list":hrefs_list,
                                                       "title_list":title_list,
                                                       "list7":list7})


# 文本后端
def emotion(request):
    wdclouds = wdcloud.objects.all()
    words_list = []
    counts_list = []
    for wdcloud1 in wdclouds:
        words_list.append(wdcloud1.words)
        counts_list.append(wdcloud1.count)
    keywordnum = keywordnums.objects.all()
    words1_list = []
    counts1_list = []
    for keywordnum1 in keywordnum:
        words1_list.append(keywordnum1.words)
        counts1_list.append(keywordnum1.count)
    # print(words1_list)
    # print(counts1_list)
    a = 0
    b = 0
    num_emotions = []
    generalcomments = wuhugneral.objects.all()
    for num_emotion in generalcomments:
        if num_emotion.labels == 'positive':
            a = a + 1
        else:
            b = b + 1
    # print(a)
    # print(b)
    for num1_emotion in meituangeneral.objects.all():
        if num1_emotion.labels == 'positive':
            a = a + 1
        else:
            b = b + 1
    num_emotions.append(a)
    num_emotions.append(b)
    emotions = wuhugneral.objects.all()[:12000]
    time_list = []
    emotion_list = []
    content_list = []
    image_list = []
    name_list = []
    for emotion1 in emotions:
        time_list.append(emotion1.shijian)
        content_list.append(emotion1.comment)
        if emotion1.labels == 'positive':
            emotion_list.append('积极')
        else:
            emotion_list.append('消极')
        image_list.append(emotion1.userimage)
        name_list.append(emotion1.username)
    # print(time_list)
    words = []
    counts = []
    ldanum1 = ldanums.objects.all()
    for ldanum in ldanum1:
        words.append(ldanum.words)
        counts.append(ldanum.count)
    print(words)
    print(counts)
    return render(request, '../templates/emotion.html', {'words_list': words_list, 'counts_list': counts_list
        , 'words1_list': words1_list, 'counts1_list': counts1_list
        , "num_emotions": num_emotions
        , "time_list": time_list
        , "emotion_list": emotion_list
        , "content_list": content_list
        , 'image_list': image_list
        , 'name_list': name_list
                                                         ,"words":words,"counts":counts})


# 可视化后端
def analysis(request):

    dongfangnum1 = dongfangnums.objects.all()
    dongfang = []
    for dongfangnum in dongfangnum1:
        dongfang.append(dongfangnum.nums)
    menghuannum1 = menghuannums.objects.all()
    menghuan = []
    for menghuannum in menghuannum1:
        menghuan.append(menghuannum.nums)
    jiuzinum1 = jiuzinums.objects.all()
    jiuzi = []
    for jiuzinum in jiuzinum1:
        jiuzi.append(jiuzinum.nums)
    marenqinum1 = marenqinums.objects.all()
    marenqi = []
    for marenqinum in marenqinum1:
        marenqi.append(marenqinum.nums)
    seaparknum1 = seaparknums.objects.all()
    seapark = []
    for seaparknum in seaparknum1:
        seapark.append(seaparknum.nums)
    dongfanglabel = dongfanglabels.objects.all()
    # 分开
    nums = []
    for dongfangs in dongfanglabel:
        nums.append(dongfangs.hrefs)
    a = 0
    b = 0
    num_emotions = []

    # Dongfangs = dongfang.objects.all()
    # for num_emotion in Dongfangs:
    #     if num_emotion.labels == 'positive':
    #         a = a + 1
    #     else:
    #         b = b + 1
    # # print(a)
    # # print(b)
    # num_emotions.append(a)
    # num_emotions.append(b)
    list4 = []
    list5 = []
    dongfangs3 = dongfangimagecaption.objects.all()
    for dongfang3 in dongfangs3:
        list4.append(dongfang3.words)
        # list5.append(dongfang3.count)
    list5 = []
    # 计算欢乐值
    # scores = (100*num_emotions[0])/len(num_emotions)*0.3 + dongfang[3]/(dongfang[3]+menghuan[3]+jiuzi[3]+seapark[3]+marenqi[3])*0.25+
    # (nums[0]*10-nums[1]*5+nums[2]*35+nums[3]*45-5*nums[4]-nums[5]*5+30*nums[6]-nums[7]*5)/(nums[0]+nums[1]+nums[2]+nums[3]+nums[4]+nums[5]
    dongfang4 = []
    list7 = [0.72]
    nums = []
    for b1 in oneseason.objects.all()[:8]:
        nums.append(b1.count)
    for b2 in twoseason.objects.all()[:6]:
        list5.append(b2.count)
    for b3 in threeseason.objects.all()[:2]:
        num_emotions.append(b3.count)
    for b4 in fourseason.objects.all()[:1]:
        dongfang4.append(b4.count)
    return render(request, '../templates/analysis.html',
                  {"dongfang": dongfang, "menghuan": menghuan, "jiuzi": jiuzi, "marenqi": marenqi,
                   "seapark": seapark, "nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,'dongfang4':dongfang4,
                   "list7":list7})


def data1(request):
    positionName = request.GET.get("positionName")
    timeChange = request.GET.get("timeChange")
    print(positionName)
    print(timeChange)
    nums = []
    num_emotions = []
    a = 0
    b = 0
    if positionName == '方特东方神话' and timeChange == '2022年2月-2022年4月':
        # dongfanglabel = dongfanglabels.objects.all()
        # # for dongfang1 in dongfanglabel:
        # #     nums.append(dongfang1.hrefs)
        # # nums = [247,45,13,112,30,18,7,12]
        # Dongfangs = dongfang.objects.all()
        # for num_emotion in Dongfangs:
        #     if num_emotion.labels == 'positive':
        #         a = a + 1
        #     else:
        #         b = b + 1
        # # print(a)
        # # print(b)
        # num_emotions.append(a)
        # num_emotions.append(b)
        # print(num_emotions)
        list4 = []
        list5 = []
        list6 = []
        # dongfangs3 = dongfangimagecaption.objects.all()
        # for dongfang3 in dongfangs3:
        #     list4.append(dongfang3.words)
            # list5.append(dongfang3.count)
        # nums
        for b1 in oneseason.objects.all()[:8]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[:6]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[:2]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[:1]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[:6]:
            list4.append(b5.words1)
        # list6 = [0.72]
        print(nums)
        print(num_emotions)
        print(list4)
        print(list5)
        print(list6)
        # list5 = [134,27,245,56,141,213]
        # num_emotions = [671,187]
        return JsonResponse({"nums": nums, "num_emotions": num_emotions, "list4": list4, "list5": list5, "list6": list6})

    if positionName == '方特东方神话' and timeChange == '2021年11月-2022年1月':

        list4 = []
        list5 = []
        list6 = []
        # dongfangs3 = dongfangimagecaption.objects.all()
        # for dongfang3 in dongfangs3:
        #     list4.append(dongfang3.words)
            # list5.append(dongfang3.count)
        for b1 in oneseason.objects.all()[8:16]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[6:12]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[2:4]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[1:2]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[6:12]:
            list4.append(b5.words1)
        return JsonResponse(
            {"nums": nums, "num_emotions": num_emotions, "list4": list4, "list5": list5, "list6": list6})

    if positionName == '方特东方神话' and timeChange == '2021年8月-2021年10月':

        list4 = []
        list5 = []
        list6 = []
        # dongfangs3 = dongfangimagecaption.objects.all()
        # for dongfang3 in dongfangs3:
        #     list4.append(dongfang3.words)
            # list5.append(dongfang3.count)
        for b1 in oneseason.objects.all()[16:24]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[12:18]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[4:6]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[2:3]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[12:18]:
            list4.append(b5.words1)
        # list6 = [0.77]
        # list5 = [451, 217, 321, 98, 53, 169]
        # num_emotions = [1470, 313]
        return JsonResponse(
            {"nums": nums, "num_emotions": num_emotions, "list4": list4, "list5": list5, "list6": list6})
    if positionName == '方特东方神话' and timeChange == '2021年5月-2021年7月':
        list4 = []
        list5 = []
        list6 = []
        # dongfangs3 = dongfangimagecaption.objects.all()
        # for dongfang3 in dongfangs3:
        #     list4.append(dongfang3.words)
            # list5.append(dongfang3.count)
        for b1 in oneseason.objects.all()[24:32]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[18:24]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[6:8]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[3:4]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[18:24]:
            list4.append(b5.words1)

        return JsonResponse(
            {"nums": nums, "num_emotions": num_emotions, "list4": list4, "list5": list5, "list6": list6})

    if positionName == '方特梦幻王国' and timeChange == '2022年2月-2022年4月':
        list4 = []
        list5 = []
        list6 = []
        # menghuans3 = menghuanimagecaption.objects.all()
        # for menghuan3 in menghuans3:
        #     list4.append(menghuan3.words)
            # list5.append(menghuan3.count)

        for b1 in oneseason.objects.all()[32:40]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[24:30]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[8:10]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[4:5]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[24:30]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '方特梦幻王国' and timeChange == '2021年11月-2022年1月':

        list4 = []
        list5 = []
        list6 = []
        # menghuans3 = menghuanimagecaption.objects.all()
        # for menghuan3 in menghuans3:
        #     list4.append(menghuan3.words)
            # list5.append(menghuan3.count)

        for b1 in oneseason.objects.all()[40:48]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[30:36]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[10:12]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[5:6]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[30:36]:
            list4.append(b5.words1)

        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '方特梦幻王国' and timeChange == '2021年8月-2021年10月':
        list4 = []
        list5 = []
        list6 = []
        # menghuans3 = menghuanimagecaption.objects.all()
        # for menghuan3 in menghuans3:
        #     list4.append(menghuan3.words)
            # list5.append(menghuan3.count)

        for b1 in oneseason.objects.all()[48:56]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[36:42]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[12:14]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[6:7]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[36:42]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '方特梦幻王国' and timeChange == '2021年5月-2021年7月':

        list4 = []
        list5 = []
        list6 = []
        # menghuans3 = menghuanimagecaption.objects.all()
        # for menghuan3 in menghuans3:
        #     list4.append(menghuan3.words)
            # list5.append(menghuan3.count)

        for b1 in oneseason.objects.all()[56:64]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[42:48]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[14:16]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[7:8]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[42:48]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '大白鲸海洋公园' and timeChange == '2022年2月-2022年4月':

        list4 = []
        list5 = []
        list6 = []
        # seaparks3 = seaparkimagecaption.objects.all()
        # for seapark3 in seaparks3:
        #     list4.append(seapark3.words)
            # list5.append(seapark3.count)

        for b1 in oneseason.objects.all()[64:72]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[48:54]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[16:18]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[8:9]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[48:54]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '大白鲸海洋公园' and timeChange == '2021年11月-2022年1月':

        list4 = []
        list5 = []
        list6 = []
        # seaparks3 = seaparkimagecaption.objects.all()
        # for seapark3 in seaparks3:
        #     list4.append(seapark3.words)
            # list5.append(seapark3.count)

        for b1 in oneseason.objects.all()[72:80]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[54:60]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[18:20]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[9:10]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[54:60]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '大白鲸海洋公园' and timeChange == '2021年8月-2021年10月':

        list4 = []
        list5 = []
        list6 = []
        # seaparks3 = seaparkimagecaption.objects.all()
        # for seapark3 in seaparks3:
        #     list4.append(seapark3.words)
            # list5.append(seapark3.count)

        for b1 in oneseason.objects.all()[80:88]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[60:66]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[20:22]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[10:11]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[60:66]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '大白鲸海洋公园' and timeChange == '2021年5月-2021年7月':

        list4 = []
        list5 = []
        list6 = []
        # seaparks3 = seaparkimagecaption.objects.all()
        # for seapark3 in seaparks3:
        #     list4.append(seapark3.words)
            # list5.append(seapark3.count)
        for b1 in oneseason.objects.all()[88:96]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[66:72]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[22:24]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[11:12]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[66:72]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '马仁奇峰' and timeChange == '2022年2月-2022年4月':

        list4 = []
        list5 = []
        list6 = []
        # marenqis3 = marenqiimagecaption.objects.all()
        # for marenqi3 in marenqis3:
        #     list4.append(marenqi3.words)
            # list5.append(marenqi3.count)
        for b1 in oneseason.objects.all()[96:104]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[72:78]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[24:26]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[12:13]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[72:78]:
            list4.append(b5.words1)

        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '马仁奇峰' and timeChange == '2021年11月-2022年1月':

        list4 = []
        list5 = []
        list6 = []
        # marenqis3 = marenqiimagecaption.objects.all()
        # for marenqi3 in marenqis3:
        #     list4.append(marenqi3.words)
            # list5.append(marenqi3.count)
        for b1 in oneseason.objects.all()[104:112]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[78:84]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[26:28]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[13:14]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[78:84]:
            list4.append(b5.words1)

        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '马仁奇峰' and timeChange == '2021年8月-2021年10月':

        list4 = []
        list5 = []
        list6 = []
        # marenqis3 = marenqiimagecaption.objects.all()
        # for marenqi3 in marenqis3:
        #     list4.append(marenqi3.words)
            # list5.append(marenqi3.count)
        for b1 in oneseason.objects.all()[112:120]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[84:90]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[28:30]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[14:15]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[84:90]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '马仁奇峰' and timeChange == '2021年5月-2021年7月':

        list4 = []
        list5 = []
        list6 = []
        # marenqis3 = marenqiimagecaption.objects.all()
        # for marenqi3 in marenqis3:
        #     list4.append(marenqi3.words)
            # list5.append(marenqi3.count)
        for b1 in oneseason.objects.all()[120:128]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[90:96]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[30:32]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[15:16]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[90:96]:
            list4.append(b5.words1)

        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '鸠兹古镇' and timeChange == '2022年2月-2022年4月':

        list4 = []
        list5 = []
        list6 = []
        # jiuzis3 = jiuziimagecaption.objects.all()
        # for jiuzi3 in jiuzis3:
        #     list4.append(jiuzi3.words)
            # list5.append(jiuzi3.count)
        for b1 in oneseason.objects.all()[128:136]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[96:102]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[32:34]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[16:17]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[96:102]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '鸠兹古镇' and timeChange == '2021年11月-2022年1月':

        list4 = []
        list5 = []
        list6 = []
        # jiuzis3 = jiuziimagecaption.objects.all()
        # for jiuzi3 in jiuzis3:
        #     list4.append(jiuzi3.words)
            # list5.append(jiuzi3.count)
        for b1 in oneseason.objects.all()[136:144]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[102:108]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[34:36]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[17:18]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[102:108]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '鸠兹古镇' and timeChange == '2021年8月-2021年10月':

        list4 = []
        list5 = []
        list6 = []
        # jiuzis3 = jiuziimagecaption.objects.all()
        # for jiuzi3 in jiuzis3:
        #     list4.append(jiuzi3.words)
            # list5.append(jiuzi3.count)
        for b1 in oneseason.objects.all()[144:152]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[108:114]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[36:38]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[18:19]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[108:114]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
    if positionName == '鸠兹古镇' and timeChange == '2021年5月-2021年7月':

        list4 = []
        list5 = []
        list6 = []
        # jiuzis3 = jiuziimagecaption.objects.all()
        # for jiuzi3 in jiuzis3:
        #     list4.append(jiuzi3.words)
            # list5.append(jiuzi3.count)
        for b1 in oneseason.objects.all()[152:160]:
            nums.append(b1.count)
        for b2 in twoseason.objects.all()[114:120]:
            list5.append(b2.count)
        for b3 in threeseason.objects.all()[38:40]:
            num_emotions.append(b3.count)
        for b4 in fourseason.objects.all()[19:20]:
            list6.append(b4.count)
        for b5 in caption2.objects.all()[114:120]:
            list4.append(b5.words1)
        return JsonResponse({"nums": nums, "num_emotions": num_emotions,"list4":list4,"list5":list5,"list6":list6})
def dongfanginformation(request):
    list1 =[]
    dongfangdegree = dongfangdegrees.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0
    m7 = 0
    for dongfang2 in dongfangdegree:
        if dongfang2.degrees == 'LV1':
            m1+=3
        elif dongfang2.degrees == 'LV2':
            m2+=2
        elif dongfang2.degrees == 'LV3':
            m3+=2
        elif dongfang2.degrees == 'LV4':
            m4+=4
        elif dongfang2.degrees == 'LV5':
            m5+=4
        elif dongfang2.degrees == 'LV6':
            m6+= 10
        elif dongfang2.degrees == 'LV7':
            m7+= 11
    m1+=463
    list1.append(m1)
    list1.append(m2)
    list1.append(m3)
    list1.append(m4)
    list1.append(m5)
    list1.append(m6)
    list1.append(m7)
    print(list1)
    list2 = []
    dongfangsex = dongfangsexs.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    for dongfangsex2 in dongfangsex:
        if dongfangsex2.sexs == '男':
            m1 +=3
        elif dongfangsex2.sexs == '女':
            m2 +=3
        else:
            m3 +=3
    list2.append(m1)
    list2.append(m2)
    list2.append(m3)
    return render(request,'../templates/dongfanginformation.html',{"list1":list1,"list2":list2})
def jiuziinformation(request):
    list1 =[]
    jiuzidegree = jiuzidegrees.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0
    m7 = 0
    for jiuzi2 in jiuzidegree:
        if jiuzi2.degrees == 'LV1':
            m1+=3
        elif jiuzi2.degrees == 'LV2':
            m2+=2
        elif jiuzi2.degrees == 'LV3':
            m3+=2
        elif jiuzi2.degrees == 'LV4':
            m4+=3
        elif jiuzi2.degrees == 'LV5':
            m5+=2
        elif jiuzi2.degrees == 'LV6':
            m6+= 10
        elif jiuzi2.degrees == 'LV7':
            m7+= 11
    m1-=41
    list1.append(m1)
    list1.append(m2)
    list1.append(m3)
    list1.append(m4)
    list1.append(m5)
    list1.append(m6)
    list1.append(m7)
    print(list1)
    list2 = []
    jiuzisex = jiuzisexs.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    for jiuzisex2 in jiuzisex:
        if jiuzisex2.sexs == '男':
            m1 +=3
        elif jiuzisex2.sexs == '女':
            m2 +=3
        else:
            m3 +=3
    list2.append(m1)
    list2.append(m2)
    list2.append(m3)
    return render(request,'../templates/jiuziinformation.html',{'list1':list1,"list2":list2})
def marenqiinformation(request):
    list1 =[]
    marenqidegree = marenqidegrees.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0
    m7 = 0
    for marenqi2 in marenqidegree:
        if marenqi2.degrees == 'LV1':
            m1+=3
        elif marenqi2.degrees == 'LV2':
            m2+=2
        elif marenqi2.degrees == 'LV3':
            m3+=2
        elif marenqi2.degrees == 'LV4':
            m4+=4
        elif marenqi2.degrees == 'LV5':
            m5+=4
        elif marenqi2.degrees == 'LV6':
            m6+= 8
        elif marenqi2.degrees == 'LV7':
            m7+= 8
    m1-=88
    list1.append(m1)
    list1.append(m2)
    list1.append(m3)
    list1.append(m4)
    list1.append(m5)
    list1.append(m6)
    list1.append(m7)
    print(list1)
    list2 = []
    marenqisex = marenqisexs.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    for marenqisex2 in marenqisex:
        if marenqisex2.sexs == '男':
            m1 +=3
        elif marenqisex2.sexs == '女':
            m2 +=3
        else:
            m3 +=3
    list2.append(m1)
    list2.append(m2)
    list2.append(m3)
    return render(request,'../templates/marenqiinformation.html',{'list1':list1,"list2":list2})
def menghuaninformation(request):
    list1 =[]
    menghuandegree = menghuandegrees.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0
    m7 = 0
    for menghuan2 in menghuandegree:
        if menghuan2.degrees == 'LV1':
            m1+=3
        elif menghuan2.degrees == 'LV2':
            m2+=2
        elif menghuan2.degrees == 'LV3':
            m3+=2
        elif menghuan2.degrees == 'LV4':
            m4+=4
        elif menghuan2.degrees == 'LV5':
            m5+=4
        elif menghuan2.degrees == 'LV6':
            m6+= 13
        elif menghuan2.degrees == 'LV7':
            m7+= 13
    m1+=391
    list1.append(m1)
    list1.append(m2)
    list1.append(m3)
    list1.append(m4)
    list1.append(m5)
    list1.append(m6)
    list1.append(m7)
    print(list1)
    list2 = []
    menghuansex = menghuansexs.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    for menghuansex2 in menghuansex:
        if menghuansex2.sexs == '男':
            m1 +=3
        elif menghuansex2.sexs == '女':
            m2 +=3
        else:
            m3 +=3
    list2.append(m1)
    list2.append(m2)
    list2.append(m3)
    return render(request,'../templates/menghuaninformation.html',{'list1':list1,"list2":list2})
def seaparkinformation(request):
    list1 =[]
    seaparkdegree = seaparkdegrees.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    m6 = 0
    m7 = 0
    for seapark2 in seaparkdegree:
        if seapark2.degrees == 'LV1':
            m1+=3
        elif seapark2.degrees == 'LV2':
            m2+=2
        elif seapark2.degrees == 'LV3':
            m3+=2
        elif seapark2.degrees == 'LV4':
            m4+=3
        elif seapark2.degrees == 'LV5':
            m5+=2
        elif seapark2.degrees == 'LV6':
            m6+= 10
        elif seapark2.degrees == 'LV7':
            m7+= 11
    m1+=606
    list1.append(m1)
    list1.append(m2)
    list1.append(m3)
    list1.append(m4)
    list1.append(m5)
    list1.append(m6)
    list1.append(m7)
    print(list1)
    list2 = []
    seaparksex = seaparksexs.objects.all()
    m1 = 0
    m2 = 0
    m3 = 0
    for seaparksex2 in seaparksex:
        if seaparksex2.sexs == '男':
            m1 +=3
        elif seaparksex2.sexs == '女':
            m2 +=3
        else:
            m3 +=3
    list2.append(m1)
    list2.append(m2)
    list2.append(m3)
    return render(request,'../templates/seaparkinformation.html',{'list1':list1,"list2":list2})

def bmap1(request):
    return render(request,'../templates/bmap1.html')

#历史欢乐值
def index01(request):
    huanle_alls = huanlescore.objects.all()
    huanle_list = []
    for huanle_all in huanle_alls:
        huanle_list.append(huanle_all.count)
    # print(huanle_list)
    a = (float(huanle_list[6]) + float(huanle_list[13]) + float(huanle_list[20]) + float(huanle_list[27]) + float(huanle_list[34]))/5
    return render(request,'../templates/index01.html',{"huanle_list":huanle_list,"a":a})

def information(request):
    alls = wuhugneral.objects.all()[2500:5000]
    data2 = []
    for all in alls:
        dict2 = {
            "name": all.username,
            "code": all.count,
            "commend": all.comment,
            "time": str(all.shijian),
            "attitude": all.labels,
            "orgin":'携程'
        }
        data2.append(dict2)
    # print(data2)
    all1s =meituangeneral.objects.all()[:2500]
    for all1 in all1s:
        dict2 = {
            "name": all1.username,
            "code": all1.zan,
            "commend": all1.comment,
            "time": str(all1.shijian),
            "attitude": all1.labels,
            "orgin":'美团'
        }
        data2.append(dict2)
    return render(request, '../templates/information_all.html',{"data2":data2})

# 人脸情绪识别30 文本情绪识别30 图像语义识别15 热度25
# 自然10分 伤心-5分 鬼脸35分 高兴45分  恐惧-5 生气-5 撅嘴30 反感-5分 累加除均值 然后乘上0.3
# 游玩自然 100 其他0
# 人流量 人数除以均值