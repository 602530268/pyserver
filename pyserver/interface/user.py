from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render_to_response
from user.models import User
from django.shortcuts import render

# 用户登录、注册接口

def login_html(request):
    return render_to_response('login.html')

def login(request):
    code = -1
    result = "invalid request"

    if request.POST:
        account = request.POST['account']
        password = request.POST['password']

        if len(password) <= 0:
            code = 1
            result = "pasword can not be nil."
        if len(account) <= 0:
            code = 1
            result = "account can not be nil."

        user = User.objects.filter(account=account, password=password).first()
        if user == None:
            code = 1
            result = "the user is not exist."
        else:
            code = 0
            result = "login success"
    return JsonResponse({"code": code,
                         "result": result})

def register_html(request):
    return render_to_response("register.html")

def register(request):
    code = -1
    result = "invalid request"

    if request.POST:
        account = request.POST['account']
        password = request.POST['password']

        user = User.objects.filter(account=account,
                                   password=password).first()
        if user == None:
            User.objects.create(account=account,
                                password=password)
            code = 0
            result = "register success."
        else:
            code = 1
            result = "the account is exist."

    return JsonResponse({"code":code,
                         "result":result})