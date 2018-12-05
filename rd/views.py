from django.shortcuts import render

# Create your views here.



def index(req):
    return render(req, 'rd/admin/index.html', {})


def print(req):
    return render(req, 'rd/admin/print.html', {})


def login(req):
    pass

def register(req):
    pass

def legout(req):
    pass