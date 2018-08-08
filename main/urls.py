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

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^notes/', notes, name='notes'),
    url(r'^upload/', upload),
    url(r'^updateNotes/', updateNotes),
    url(r'^addNotes/', addNotes, name='add'),
    url(r'^delNotes/', delNotes),
    url(r'^filelist/(?P<fn>\w+.\w+)', filelist, name="filelist"),
    url(r'^show_alldata_intable/', get_data, name="get_data"),
]
