from django.shortcuts import render,redirect
from django.contrib import sessions
from rd.models import *

# Create your views here.



def index(req):
    return render(req, 'rd/admin/index.html', {})


def print(req):
    return render(req, 'rd/admin/print.html', {})


def login(req):
    if req.method == 'GET':
        # 判断session是否有记录
        return render(req, 'rd/admin/login.html', {})
    else:
        # 对账号密码进行验证
        return redirect('rd:index')

def register(req):
    pass

def legout(req):
    pass