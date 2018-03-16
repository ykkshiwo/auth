from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import os
# Create your views here.


def regist_(request):
    print(" diao yong")
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, email, password)
        user = User.objects.create_user(username=str(username), email=str(email), password=str(password))
        user.save()
        return HttpResponse("regist success")
    else:
        return render(request, 'regist.html')


def login_(request):
    print("diaoyong login")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=str(username), password=str(password))
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("login success")
        else:
            return HttpResponse("something wrong")
    else:
        return render(request, 'login.html')


def logout_(request):
    logout(request)
    return HttpResponse("已经退出")


@login_required(login_url='/cant')
def are_you_login(request):
    return render(request, 'index.html')


def cant(request):
    return render(request, 'cant.html')


@login_required(login_url='/cant')
def upload(request):
    if request.method == 'POST':
        obj = request.FILES.get('pictures')
        f = open(os.path.join('D:/upload', obj.name), 'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()
        return HttpResponse('上传成功')
    else:
        return render(request, 'upload.html')