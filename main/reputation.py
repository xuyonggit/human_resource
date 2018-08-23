# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import tb_from_user


"""
信用中心
"""


def index(request):
    return render(request, "Reputation.html")


#
@csrf_exempt
def getFromUserInfo(request):
    if request.method == 'POST':
        info_list = []
        userdata = tb_from_user.objects.all().order_by("-reputation").values()
        print("Get reputation : {}".format(list(userdata)))
        for d in range(len(userdata)):
            info_dic = {}
            info_dic['id'] = d + 1
            info_dic['username'] = userdata[d]['username']
            info_dic['reputation'] = userdata[d]['reputation']
            info_dic['recommend_count'] = userdata[d]['recommend_count']
            info_list.append(info_dic)

        return HttpResponse(json.dumps(info_list))
