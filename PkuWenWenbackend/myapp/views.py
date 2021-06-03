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
import json

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
@csrf_exempt
def getSchoolIndex(request):
    retdata = {}
    schools = models.School.objects.values()
    retdata['schoollist'] = list(schools)
    return JsonResponse(retdata)


@csrf_exempt
def openSchool(request):
    schoolName = request.POST.get('school', '信息科学技术学院')
    courses = [ {'date': '更新于 2021-06-03 15:56:00', 'title': 'course1 from backend openSchool'}, {'date': '更新于 2021-06-03 15:56:00', 'title': 'course2 from backend openSchool'} ]
    courses = json.JSONEncoder(ensure_ascii=False).encode(courses)
    print("将courses发回前端")
    return JsonResponse({'retCode': 1, 'courses': courses})


@csrf_exempt
def openCourse(request):
    courseName = request.POST.get('course', '软件工程')
    questions = [ 
        {'date': '更新于 2021-06-03 15:56:00', 'title': 'Question1 from backend', 'content': 'c1', 'stars': 58, 'link': 'l1'}, 
        {'date': '更新于 2021-06-03 15:56:00', 'title': 'Question2 from backend', 'content': 'c2', 'stars': 66, 'link': 'l2'}, 
        ]
    questions = json.JSONEncoder(ensure_ascii=False).encode(questions)
    return JsonResponse({'retCode': 1, 'questions': questions})


@csrf_exempt
def openQuestion(request):
    courseName = request.POST.get('question', '默认问题')

    curQuestion = { 'publisher': 'alice', 'title': 'ahhhhhhh', 'detail': '咆哮啊啊啊', 'proNum': 2, 'conNum': 1, 'subscribeNum': 3,}
    curQuestion = json.JSONEncoder(ensure_ascii=False).encode(curQuestion)
    curAnswer = { 'publisher': 'bob', 'title': 'hahahahahaha', 'detail': '哈哈哈哈哈', 'proNum': 6, 'conNum': 6, 'subscribeNum': 12,} 
    # 现在只显示一个问题和一个答案, 如果我们想要看一个问题的所有答案, 只需要搞成list of dict 就可以了 暂时不实现
    curAnswer = json.JSONEncoder(ensure_ascii=False).encode(curAnswer)

    return JsonResponse({'retCode': 1, 'curQuestion': curQuestion, 'curAnswer': curAnswer})


@csrf_exempt
def submitQuestion(request):
    questionTitle = request.POST.get('title', '缺少标题')
    questionDate1 = request.POST.get('date1', '0000-00-00')
    questionDate2 = request.POST.get('date2', '00:00:00')
    questionDetail = request.POST.get('detail', '缺少问题描述')
    # 此处应该把问题存到数据库里
    return JsonResponse({'retCode': 1, 'title': questionTitle, 'detail': questionDetail})

'''
这个关注课程功能不仅不重要而且很麻烦我先不写了。
@csrf_exempt
def AddFollowCourse(request):
    course_name = request.POST.get('course_name')
    user_name = request.POST.get('userName')
    user_obj = models.UserModel.objects.get(userName = user_name)
    user_obj.
'''
