from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from .models import notes as nt
from .models import tb_from_user
from human_source.settings import FILESPATH
import os
import json

# 创建简历附件目录
if not os.path.exists(FILESPATH):
    os.mkdir(FILESPATH)


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
            dic1['position'] = d['position']

            List_data.append(dic1)
            num += 1

        return HttpResponse(json.dumps(List_data))


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        obj = request.FILES.get('file')
        filename = obj.name
        num = 1
        while os.path.exists(os.path.join(FILESPATH, filename)):
            filename = "{}_{}.{}".format(obj.name.split(".")[0], num, obj.name.split(".")[1])
            num += 1
        with open(os.path.join(FILESPATH, filename), 'wb') as f:
            for chunk in obj.chunks():
                f.write(chunk)
        return HttpResponse(json.dumps({"state": "success", "lstOrderImport": "2"}))


@csrf_exempt
def updateNotes(request):
    if request.method == 'POST':
        uid = request.POST.get('id', "")
        name = request.POST.get('name', "")
        from_user = request.POST.get('from_user', "")
        filename = request.POST.get('filename', "")
        position = request.POST.get("position", "")
        source_data = nt.objects.get(id=uid)
        filename_old = source_data.notes
        if filename == filename_old:
            pass
        else:
            # 执行简历文件替换
            if os.path.exists(os.path.join(FILESPATH, filename_old)):
                os.remove(os.path.join(FILESPATH, filename_old))
            source_data.notes = filename
        source_data.name = name
        source_data.from_user = from_user
        source_data.position = position
        source_data.save()
        return HttpResponse(json.dumps({"state": "success"}))


# 新增记录
@csrf_exempt
def addNotes(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get("name", "")
        from_user = request.POST.get("from_user", "")
        objname = request.POST.get("filename", "")
        position = request.POST.get("position", "")
        filename = objname
        # 添加数据是创建推荐人数据
        tmp_data_from_user = tb_from_user.objects.filter(username=from_user)
        if not tmp_data_from_user:
            tb_from_user.objects.create(
                username=from_user,
                recommend_count=1
            )
        # 文件重名则重命名
        num = 1
        while os.path.exists(os.path.join(FILESPATH, filename)):
            filename = "{}_{}.{}".format(objname.split(".")[0], num, objname.split(".")[1])
            num += 1
        if num == 2:
            filename = objname
        else:
            filename = "{}_{}.{}".format(objname.split(".")[0], num-2, objname.split(".")[1])
        if not name:
            return HttpResponse(json.dumps({"state": "error", 'detail': "姓名不能为空"}))
        if not from_user:
            return HttpResponse(json.dumps({"state": "error", 'detail': "推荐人不能为空"}))
        if not filename:
            return HttpResponse(json.dumps({"state": "error", 'detail': "简历不能为空"}))
        # 创建简历数据
        nt.objects.create(
            name=name,
            from_user=from_user,
            notes=filename,
            position=position
        )
        return HttpResponse(json.dumps({"state": "success"}))


@csrf_exempt
def delNotes(request):
    if request.method == 'POST':
        uid = request.POST.get('uid', "")
        filename = request.POST.get('notes', "")
        if uid:
            p = nt.objects.get(id=uid)
            p.delete()
        if filename:
            filename = filename.split(">")[1].split("<")[0]
            if os.path.exists(os.path.join(FILESPATH, filename)):
                os.remove(os.path.join(FILESPATH, filename))
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
