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
        info_dic = {}
        userdata = tb_from_user.objects.all().values()
        for d in userdata:
            info_dic[d['username']] = {}
            info_dic[d['username']]['reputation'] = d['reputation']
            info_dic[d['username']]['recommend_count'] = d['recommend_count']

        return HttpResponse(json.dumps(info_dic))