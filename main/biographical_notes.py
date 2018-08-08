from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from .models import notes as nt
from human_source.settings import FILESPATH
import os
import json


def index(request):
    return render(request, "Index.html")


@csrf_exempt
def notes(request):
    return render(request, 'biographical.html')


@csrf_exempt
def get_data(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        from_user = request.POST.get("from_user", "")
        print(request.POST)
        if name and not from_user:
            res_data = nt.objects.filter(name=name)
        elif not name and from_user:
            res_data = nt.objects.filter(from_user=from_user)
        elif not name and not from_user:
            res_data = nt.objects.all()
        else:
            res_data = nt.objects.filter(name=name, from_user=from_user)
        List_data = []
        num = 1
        for d in res_data.values():
            dic1 = {}
            dic1['id'] = num
            dic1['uid'] = d['id']
            dic1['name'] = d['name']
            dic1['from_user'] = d['from_user']
            dic1['notes'] = "<a href=\"/biog/filelist/{}\">{}</a>".format(d['notes'], d['notes'])

            List_data.append(dic1)
            num += 1

        return HttpResponse(json.dumps(List_data))


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        obj = request.FILES.get('file')
        if os.path.exists(os.path.join(FILESPATH, obj.name)):
            os.remove(os.path.join(FILESPATH, obj.name))
        with open(os.path.join(FILESPATH, obj.name), 'wb') as f:
            for chunk in obj.chunks():
                f.write(chunk)
        return HttpResponse(json.dumps({"status": 0, "lstOrderImport": "2"}))


@csrf_exempt
def updateNotes(request):
    if request.method == 'POST':
        uid = request.POST.get('id', "")
        name = request.POST.get('name', "")
        from_user = request.POST.get('from_user', "")
        filename = request.POST.get('filename', "")
        source_data = nt.objects.get(id=uid)
        source_data.name = name
        source_data.from_user = from_user
        source_data.notes = filename
        source_data.save()
        return HttpResponse(json.dumps({"state": "success"}))


@csrf_exempt
def addNotes(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get("name", "")
        from_user = request.POST.get("from_user", "")
        filename = request.POST.get("filename", "")
        print(name, from_user, filename)
        if not name:
            return HttpResponse(json.dumps({"state": "error", 'detail': "姓名不能为空"}))
        if not from_user:
            return HttpResponse(json.dumps({"state": "error", 'detail': "推荐人不能为空"}))
        if not filename:
            return HttpResponse(json.dumps({"state": "error", 'detail': "简历不能为空"}))

        nt.objects.create(
            name=name,
            from_user=from_user,
            notes=filename
        )
        return HttpResponse(json.dumps({"state": "success"}))


@csrf_exempt
def delNotes(request):
    if request.method == 'POST':
        uid = request.POST.get('uid', "")
        if uid:
            p = nt.objects.get(id=uid)
            p.delete()
        return HttpResponse(json.dumps({"state": "success"}))


def filelist(request, fn):
    filename = fn
    print(os.path.join(FILESPATH, filename))
    if filename and os.path.exists(os.path.join(FILESPATH, filename)):
        file = open(os.path.join(FILESPATH, filename), 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
        return response
    return render(request, '404.html')
