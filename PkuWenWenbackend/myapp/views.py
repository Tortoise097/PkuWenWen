from django.shortcuts import render
from . import models
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.tokens import default_token_generator
import json
import requests
import json
from django.core.mail import send_mail
from django.conf import settings
import re
import random

# Create your views here.

# 注册（使用了Django内助的邮箱验证功能）
@csrf_exempt
def register(request):
    userName = request.POST.get('userName', 'username')
    password = request.POST.get('password', 'xxx')
    email = request.POST.get('email', 'undefined')
    res = {'retCode': 0, 'message': ''}

    obj = models.UserModel.objects.filter(userName=userName)
    objmail = models.UserModel.objects.filter(email=email)

    if obj.count() == 0 and objmail.count() == 0:
        mailret = send_mail('PkuWenWen注册', '您正在进行PkuWenWen注册，如果不是您亲自操作，请及时联系本邮箱',
                            'se_5group@163.com', [email], fail_silently=False)

        if mailret == 1:
            models.UserModel.objects.create(userName=userName, password=password,email=email)
            obj = models.UserModel.objects.get(userName=userName)
            # obj.collectList.remove('-1')
            obj.save()
            res['retCode'] = 1
            res['message'] = '注册成功'

        else:
            res['retCode'] = 2
            res['message'] = '请输入正确的邮箱地址'

    else:
        res['retCode'] = 0
        res['message'] = '用户名或邮箱已注册'

    return JsonResponse({'register': res})

# 登录：登录之后会自动跳转到SchoolIndex页
@csrf_exempt
def login(request):
    userName = request.POST.get('userName', 'username')
    password = request.POST.get('password', 'xxx')
    res = {'retCode': 0, 'message': ''}
    print("userName = {}, password = {}".format(userName,password))
    obj = models.UserModel.objects.filter(userName=userName)

    if obj.count() == 0:
        res['retCode'] = 0
        res['message'] = '用户不存在'
        print('用户不存在')
    else:
        obj = models.UserModel.objects.get(userName=userName)
        if obj.password == password:
            res['retCode'] = 1
            res['message'] = '成功登录'
            print("登陆成功")
        else:
            res['retCode'] = 2
            res['message'] = '密码错误'
            print("密码错误")
    return JsonResponse({'login': res})
    # return HttpResponse(json.dumps({'login': res}))

