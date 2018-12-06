from django.shortcuts import render,redirect
from django.contrib import sessions
from rd.models import *

# Create your views here.


def index(req):
    return render(req, 'rd/admin/index.html', {})


def login(req):
    username = req.session.get("username", None)
    if req.method == 'GET':
        # 判断session是否有记录
        if username is None:
            return render(req, 'rd/admin/login.html', {})
        else:
            try:
                user = BUser.objects.get(name=username)
            except:
                return render(req, 'rd/admin/login.html', {})
            return redirect('index:index')
    else:
        # 对账号密码进行验证
        username = req.POST.get('username', None)
        password = req.POST.get('password', None)
        if username and password:
            try:
                user = BUser.objects.filter(name=username).filter(passwrod=password)
            except:
                message = "请输入正确的账号和密码。"
                return render(req, 'rd/admin/loginMessage.html', {'message':message})
            if user.count() >= 1:
                req.session["username"] = username
                return redirect('rd:index')
            else:
                message = "请输入正确的账号和密码。"
                return render(req, 'rd/admin/loginMessage.html', {'message':message})
        else:
            message = "请输入正确的账号和密码。"
            return render(req, 'rd/admin/loginMessage.html', {'message':message})


def register(req):
    pass

def legout(req):
    pass