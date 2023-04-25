from django.db import models


class huati_rank(models.Model):
    rank = models.CharField(max_length=64, null=True)
    topic_href = models.CharField(max_length=64, null=True)
    topic_title = models.CharField(max_length=64, null=True)
    taolun = models.CharField(max_length=64, null=True)
    read = models.CharField(max_length=64, null=True)


class hot_rank(models.Model):
    rank = models.CharField(max_length=64, null=True)
    hot_title = models.CharField(max_length=64, null=True)
    hot_href = models.CharField(max_length=64, null=True)
    hot_num = models.CharField(max_length=64, null=True)


class wb_search(models.Model):
    times = models.CharField(max_length=64, null=True)
    herf = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class lianghui_topic(models.Model):
    href = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    taolun = models.CharField(max_length=64, null=True)
    read = models.CharField(max_length=64, null=True)


class User(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个主键
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码
    email = models.CharField(max_length=32)  # 邮箱


class feel_analyse_2(models.Model):
    text = models.CharField(max_length=64, null=True)
    sentiment_label = models.CharField(max_length=64, null=True)
    sentiment_key = models.CharField(max_length=64, null=True)
    positive_probs = models.CharField(max_length=64, null=True)
    negative_probs = models.CharField(max_length=64, null=True)


class tuerqi_topic(models.Model):
    href = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    taolun = models.CharField(max_length=64, null=True)
    read = models.CharField(max_length=64, null=True)


class ershida_topic(models.Model):
    href = models.CharField(max_length=64, null=True)
    title = models.CharField(max_length=64, null=True)
    taolun = models.CharField(max_length=64, null=True)
    read = models.CharField(max_length=64, null=True)


class lianghui_search(models.Model):
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class tuerqi_search(models.Model):
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class ershida_search(models.Model):
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class task_list_1(models.Model):
    num = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)


class feel_analyse_test(models.Model):
    nums = models.CharField(max_length=64, null=True)
    shijian = models.CharField(max_length=64, null=True)
    # sentiment_key = models.CharField(max_length=64, null=True)
    # positive_probs = models.CharField(max_length=64, null=True)
    # negative_probs = models.CharField(max_length=64, null=True)

# feel_analyse_result是两会，2是土耳其，3是二十大
# 4，5，6等是文章分类
class feel_analyse_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)

class feel_analyse_result_2(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class feel_analyse_result_3(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class remenzongyi_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class mingxingbagua_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)



class shehuiredian_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)



class tiyusaishi_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)



class meishilvyou_result(models.Model):
    jiji = models.CharField(max_length=64, null=True)
    zhongxing = models.CharField(max_length=64, null=True)
    xiaoji = models.CharField(max_length=64, null=True)
    num = models.CharField(max_length=64, null=True)
    key_s = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)



class remenzongyi_search(models.Model):
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class mingxingbagua_search(models.Model):
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class shehuiredian_search(models.Model):
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class tiyusaishi_search(models.Model):
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class meishilvyou_search(models.Model):
    time = models.CharField(max_length=64, null=True)
    href = models.CharField(max_length=64, null=True)
    author = models.CharField(max_length=64, null=True)
    content = models.CharField(max_length=64, null=True)
    share_num = models.CharField(max_length=64, null=True)
    pingllun_num = models.CharField(max_length=64, null=True)
    dianzan_num = models.CharField(max_length=64, null=True)


class huati_add_5(models.Model):
    a_j = models.CharField(max_length=64, null=True)#热门综艺
    a_z = models.CharField(max_length=64, null=True)
    a_x= models.CharField(max_length=64, null=True)
    b_j = models.CharField(max_length=64, null=True)#明星八卦
    b_z = models.CharField(max_length=64, null=True)
    b_x= models.CharField(max_length=64, null=True)
    c_j = models.CharField(max_length=64, null=True)#社会热点
    c_z = models.CharField(max_length=64, null=True)
    c_x= models.CharField(max_length=64, null=True)
    d_j = models.CharField(max_length=64, null=True)#体育赛事
    d_z = models.CharField(max_length=64, null=True)
    d_x= models.CharField(max_length=64, null=True)
    e_j = models.CharField(max_length=64, null=True)#美食旅游
    e_z = models.CharField(max_length=64, null=True)
    e_x= models.CharField(max_length=64, null=True)

    jiji_add= models.CharField(max_length=64, null=True)
    zhongxing_add= models.CharField(max_length=64, null=True)
    xiaoji_add= models.CharField(max_length=64, null=True)

    all_add= models.CharField(max_length=64, null=True)
    zhishu= models.CharField(max_length=64, null=True)



class huati_add_3(models.Model):
    f_j = models.CharField(max_length=64, null=True)#两会
    f_z = models.CharField(max_length=64, null=True)
    f_x= models.CharField(max_length=64, null=True)
    g_j = models.CharField(max_length=64, null=True)#土耳其地震
    g_z = models.CharField(max_length=64, null=True)
    g_x= models.CharField(max_length=64, null=True)
    h_j = models.CharField(max_length=64, null=True)#二十大
    h_z = models.CharField(max_length=64, null=True)
    h_x= models.CharField(max_length=64, null=True)

    jiji_add= models.CharField(max_length=64, null=True)
    zhongxing_add= models.CharField(max_length=64, null=True)
    xiaoji_add= models.CharField(max_length=64, null=True)

    all_add= models.CharField(max_length=64, null=True)
    zhishu= models.CharField(max_length=64, null=True)