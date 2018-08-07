from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import notes as nt


def index(request):
    return render(request, "base.html")


@csrf_exempt
def notes(request):
    return render(request, 'biographical.html')


@csrf_exempt
def get_data(request):
    if request.method == 'POST':
        print(request.POST)
        res_data = nt.objects.all()
        List_data = []
        num = 1
        for d in res_data.values():
            dic1 = {}
            dic1['id'] = num
            dic1['name'] = d['name']
            dic1['from_user'] = d['from_user']
            dic1['notes'] = "<a href=\"/biog/notes/{}\">{}</a>".format(d['notes'], d['notes'])

            List_data.append(dic1)
            num += 1

        return HttpResponse(json.dumps(List_data))


def upload(request):
    return render(request, 'biographical.html')
