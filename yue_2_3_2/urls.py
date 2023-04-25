"""yue_1_20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.templatetags.static import static
from django.urls import path
from app01 import views
# from yue_2_3_2 import settings
# from yue_2_3_2_end import static
# from django.contrib import admin


urlpatterns = [
    # 跳转登录页面
    # path('',views.login,name='login'),
    # echarts图表
    path('chart/pie_1/', views.chart_pie_1),
    path('chart/pie_2/', views.chart_pie_2),
    path('chart/line/', views.chart_line),
    path('test/k/', views.test_k),

    # 页面跳转
    path('login/', views.login),
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('logout/', views.logout),

    path('index_2/', views.index_2),
    path('', views.login),
    path('layouts/', views.layouts),
    path('analyse/', views.analyse),
    path('analyse_2/', views.analyse_2),
    path('project_detail/', views.project_detail),
    path('trace/', views.trace),
    path('trace_2/', views.trace_2),
    path('test/', views.test),

    # 任务管理
    # path('orm/', views.orm),          测试用例
    path('task_list/', views.task_list),
    path('task_add/', views.task_add),
    path('task_delete/', views.task_delete),
    # path('task_delete/', views.task_delete),
    #     综合后期代码
    path('guanli_task/', views.guanli_task),
    path('id_guanli/', views.id_guanli),
    # path('pinglun/', views.pinglun),
    # 登录注册
    # path('admin/', admin.site.urls),

    path('new_index/', views.new_index),
    path('new_trace/', views.new_trace),
    path('new_analyse/', views.new_analyse),
    path('new_id_guanli/', views.new_id_guanli),
    path('new_layout/', views.new_layout),

    path('new_layout_2/', views.new_layout_2),
    path('bdchart/', views.bdchart),


    #ajax取数据
    path('chart/pie/', views.chart_pie),
]
