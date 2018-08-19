"""human_source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.biographical_notes import *
import main.reputation as rep

urlpatterns = [
    url(r'^$', index, name='index'),
    # ------------------- 简历库 ---------------------
    # 简历库首页
    url(r'^notes/', notes, name='notes'),
    # 上传简历附件
    url(r'^upload/', upload),
    # 获取级别基数
    url(r'^get_level_basenum/', get_level_basenum),
    # 更新数据
    url(r'^updateNotes/', updateNotes),
    # 添加简历记录
    url(r'^addNotes/', addNotes, name='add'),
    # 删除简历记录
    url(r'^delNotes/', delNotes),
    # 下载简历附件列表
    url(r'^filelist/(?P<fn>\w+.\w+)', filelist, name="filelist"),
    # 全局数据
    url(r'^show_alldata_intable/', get_data, name="get_data"),
    # --------------------- END ------------------------
    # 信用中心
    url(r'^reputation/', rep.index, name="reputation"),
    url(r'^getFromUserInfo/', rep.getFromUserInfo, name="getuserinfo")
]
