from django.urls import path
from . import views

#
urlpatterns = [
    path('', views.login, name='login'),
    path('look', views.look, name='look'),
    path('register', views.register, name='register'),
    path('verification', views.verification, name='verification'),
    path('forget', views.forget, name='forget'),
    path('forget_pwd', views.forget_pwd, name='forget_pwd'),
    path('register_1', views.register_1, name='register_1'),  ## 至此
    # path('test1', views.test1, name='test1'),
    path('test2', views.test2, name='test2'),
    path('qingganfenxi', views.qingganfenxi, name='qingganfenxi'),
    path('index', views.index, name='index'),
    path('image', views.image, name='image'),
    path('emotion', views.emotion, name='emotion'),
    # path('addcomment',views.addcomment,name='addcomment'),
    path('hotword', views.hotword, name='hotword'),
    path('posword', views.posword, name='posword'),
    path('negword', views.negword, name='negword'),
    path('analysis', views.analysis, name='analysis'),
    path('data1', views.data1),
    path('dongfanginformation', views.dongfanginformation),
    path('jiuziinformation', views.jiuziinformation),
    path('menghuaninformation', views.menghuaninformation),
    path('seaparkinformation', views.seaparkinformation),
    path('marenqiinformation', views.marenqiinformation),
    path('bmap1', views.bmap1),
    path('index01', views.index01),
    path('information', views.information),

]
