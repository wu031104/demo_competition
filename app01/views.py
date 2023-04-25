import json
from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app01 import models


#
# from django.contrib import admin
# from . import models
#
# admin.site.register(models.User)


# echarts图表统计
def chart_pie_1(request):
    """ 构造饼图1的数据 """

    db_data_list = [
        {"value": 2048, "name": '积极'},
        {"value": 1735, "name": '消极'},
    ]

    result = {
        "status": True,
        "data": db_data_list
    }
    return JsonResponse(result)


def chart_pie_2(request):
    """ 构造饼图2的数据 """

    db_data_list = [
        {"value": 2048, "name": '娱乐'},
        {"value": 1735, "name": '体育'},
        {"value": 1735, "name": '科技'},
        {"value": 1735, "name": '景点'},
        {"value": 1735, "name": '政治'},
        {"value": 1735, "name": '明星'},
        {"value": 1735, "name": '自然界'},
    ]

    result = {
        "status": True,
        "data": db_data_list
    }
    return JsonResponse(result)


def chart_line(request):
    legend = ["上海", "广西"]
    series_list = [
        {
            "name": '上海',
            "type": 'line',
            "stack": 'Total',
            "data": [5, 20, 36, 10, 10, 10]
        },
        {
            "name": '广西',
            "type": 'line',
            "stack": 'Total',
            "data": [45, 10, 66, 40, 20, 50]
        }
    ]
    x_axis = ['1月', '2月', '4月', '5月', '6月', '7月']

    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def test_k(request):
    return HttpResponse("nicai")


# 普通页面跳转

def index_2(request):
    """ 数据统计页面 """
    data_list_1 = models.hot_rank.objects.all()
    huati_add_5 = models.huati_add_5.objects.all()
    # huati_num_3 = models.huati_add_3.objects.all()
    return render(request, 'index_2.html',
                  {'data_list': data_list_1, 'huati_add_5': huati_add_5})


def register(request):
    # 定义一个错误提示为空
    error_name = ''
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_list = models.User.objects.filter(username=user)
        if user_list:
            # 注册失败
            error_name = '%s用户名已经存在了' % user
            # 返回到注册页面，并且把错误信息报出来
            return render(request, 'register.html', {'error_name': error_name})
        else:
            # 数据保存在数据库中，并返回到登录页面
            user = models.User.objects.create(username=user,
                                              password=password,
                                              email=email)
            user.save()
            return redirect('/login/')
    return render(request, 'register.html')


def login(request):
    # 定一个为空的错误接收
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 判断数据库中有没有账号密码
        ret = models.User.objects.filter(username=username, password=password)
        if ret:
            # 登录到安静博客
            return redirect('/index_2/')
        else:
            # 登录失败
            error_msg = '用户名或密码错误，请重新输入！'
    return render(request, 'login.html', {'error_msg': error_msg})


def logout(request):
    pass
    return redirect('/login/')


def layouts(request):
    return render(request, 'layouts.html')


def analyse(request):
    data_list_0 = models.huati_rank.objects.all()
    data_list_1 = models.feel_analyse_result.objects.all()  # 两会
    data_list_2 = models.feel_analyse_result_2.objects.all()  # 土耳其
    data_list_3 = models.feel_analyse_result_3.objects.all()  # 二十大
    # 三个重点话题的相关话题
    data_list_4 = models.lianghui_topic.objects.all()
    data_list_5 = models.tuerqi_topic.objects.all()
    data_list_6 = models.ershida_topic.objects.all()

    huati_add_5 = models.huati_add_5.objects.all()

    return render(request, 'analyse.html',
                  {'data_list_0': data_list_0, 'data_list_1': data_list_1, 'data_list_2': data_list_2,
                   'data_list_3': data_list_3, 'data_list_4': data_list_4, 'data_list_5': data_list_5,
                   'data_list_6': data_list_6, 'huati_add_5': huati_add_5})


def analyse_2(request):
    data_list_1 = models.remenzongyi_result.objects.all()  # 热门综艺
    data_list_2 = models.mingxingbagua_result.objects.all()  # 明星八卦
    data_list_3 = models.shehuiredian_result.objects.all()  # 社会热点
    data_list_4 = models.tiyusaishi_result.objects.all()  # 体育赛事
    data_list_5 = models.meishilvyou_result.objects.all()  # 美食旅游

    return render(request, 'analyse_2.html',
                  {'data_list_1': data_list_1, 'data_list_2': data_list_2,
                   'data_list_3': data_list_3, 'data_list_4': data_list_4, 'data_list_5': data_list_5})


def project_detail(request):
    return render(request, 'project_detail.html')


def trace(request):
    data_list_0 = models.huati_rank.objects.all()
    data_list_1 = models.feel_analyse_result.objects.all()  # 两会
    data_list_2 = models.feel_analyse_result_2.objects.all()  # 土耳其
    data_list_3 = models.feel_analyse_result_3.objects.all()  # 二十大
    # 三个重点话题的相关话题
    data_list_4 = models.lianghui_topic.objects.all()
    data_list_5 = models.tuerqi_topic.objects.all()
    data_list_6 = models.ershida_topic.objects.all()

    huati_add_3 = models.huati_add_3.objects.all()

    return render(request, 'trace.html',
                  {'data_list_0': data_list_0, 'data_list_1': data_list_1, 'data_list_2': data_list_2,
                   'data_list_3': data_list_3, 'data_list_4': data_list_4, 'data_list_5': data_list_5,
                   'data_list_6': data_list_6, 'huati_add_3': huati_add_3})


def trace_2(request):
    data_list_0 = models.huati_rank.objects.all()
    data_list_1 = models.feel_analyse_result.objects.all()  # 两会
    data_list_2 = models.feel_analyse_result_2.objects.all()  # 土耳其
    data_list_3 = models.feel_analyse_result_3.objects.all()  # 二十大
    # 三个重点话题的相关话题
    data_list_4 = models.lianghui_topic.objects.all()
    data_list_5 = models.tuerqi_topic.objects.all()
    data_list_6 = models.ershida_topic.objects.all()

    return render(request, 'trace_2.html',
                  {'data_list_0': data_list_0, 'data_list_1': data_list_1, 'data_list_2': data_list_2,
                   'data_list_3': data_list_3, 'data_list_4': data_list_4, 'data_list_5': data_list_5,
                   'data_list_6': data_list_6})


def task_list(request):
    """任务列表"""
    queryset = models.task_list_1.objects.all()
    return render(request, 'task_list.html', {'queryset': queryset})


def task_add(request):
    """任务列表"""

    if request.method == "GET":
        return render(request, 'task_list.html')
    # 获取用户提交的数据
    num = request.POST.get("num")
    name = request.POST.get("name")
    time = request.POST.get("time")

    # 添加到数据库
    models.task_list_1.objects.create(num=num, name=name, time=time)

    return redirect("/task_list/")


def task_delete(request):
    # 获取ID
    # http: // 127.0.0.1: 8000 / task_delete /?nid = 1
    nid = request.GET.get('nid')
    # 删除
    models.task_list_1.objects.filter(id=nid).delete()

    # 重定向回任务列表
    return redirect("/task_list/")


# 后期代码
def guanli_task(request):
    return render(request, 'guanli_task.html')


def id_guanli(request):
    return render(request, 'id_guanli.html')


def test(request):
    """ 数据统计页面 """
    data_list_0 = models.huati_rank.objects.all()
    data_list_1 = models.feel_analyse_result.objects.all()  # 两会
    data_list_2 = models.feel_analyse_result_2.objects.all()  # 土耳其
    data_list_3 = models.feel_analyse_result_3.objects.all()  # 二十大
    # 三个重点话题的相关话题
    data_list_4 = models.lianghui_topic.objects.all()
    data_list_5 = models.tuerqi_topic.objects.all()
    data_list_6 = models.ershida_topic.objects.all()

    return render(request, 'test.html',
                  {'data_list_0': data_list_0, 'data_list_1': data_list_1, 'data_list_2': data_list_2,
                   'data_list_3': data_list_3, 'data_list_4': data_list_4, 'data_list_5': data_list_5,
                   'data_list_6': data_list_6})


def chart_pie(request, huati_num_5=models.huati_add_5.objects.all()):
    """ 构造饼图的数据 """

    db_data_list = [
        {"value": {{huati_num_5.jiji_add}}, "name": '积极'},
        {"value": {{huati_num_5.zhongxing_add}}, "name": '中性'},
        {"value": {{huati_num_5.xiaoji_add}}, "name": '消极'},
    ]

    result = {
        "status": True,
        "data": db_data_list
    }
    return JsonResponse(result)


def new_index(request):
    return render(request, 'new_index.html')


def new_trace(request):
    return render(request, 'new_trace.html')


def new_analyse(request):
    return render(request, 'new_analyse.html')


def new_id_guanli(request):
    return render(request, 'new_id_guanli.html')


def new_layout(request):
    return render(request, 'new_layout.html')


def new_layout_2(request):
    return render(request, 'new_layout_2.html')


def bdchart(request):
    return render(request, 'bdchart.html')
