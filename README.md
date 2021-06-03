README

前端：所有代码都砸pkuwenwenfrontend里（不用大写是因为vue不支持大写）
to run the frontend in development procedure, `cd pkuwenwenfrontend` then `yarn serve`

后端：全都在PkuWenWenbackend里
to tunn the backend in development procedure `cd PkuWenWenbackend` then `python manage.py runserver`

# QA:
## how to overcome CORS error
read this part in `PkuWenWenbackend/PkuWenWenbackend/settings.py`\
```python
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

######################### Add these about CORS #####################################
CORS_ORIGIN_ALLOW_ALL = False
# CORS_ORIGIN_WHITELIST = ("127.0.0.1:8080")
CORS_ALLOWED_ORIGINS = [
    "http://10.2.63.187:8080",
    "http://10.0.32.212:8080",
    "http://localhost:8080",
]

CORS_ALLOW_METHODS = (
    'GET',
    'POST',

)
######################### Add these about CORS #####################################
```
the word cors appear in 9 places in the above section, find all of them!\
once you understand it, add your own address in `CORS_ALLOWED_ORIGINS`, which should appear when you run the frontend by using\
`npm run serve` or `yarn serve`


## how front end interact with backend?
1. front end sending POST requests to backend using backend url with interface :\
   in this case, the url is `app.config.globalProperties.$url = 'http://127.0.0.1:8000'`defined in `main.js` \
   and the interface is `/openSchool`\
   the script will execute till the line of`.then((response) => {` then wait response from backend.
```javascript
//this part exists in SchoolIndex.vue
openSchool (school) {
    // console.log(`dash: ${school.id}`);
    // this.$router.push({
    //   name: 'CourseIndex',
    //   params: {url:school.link,id:school.id}
    // })
    var post_request = new FormData()
    post_request.append('school', school)
    let _this = this;
    this.$http
        .request({
            url: this.$url + '/openSchool',
            method: 'post',
            data: post_request,
            headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((response) => {
            console.log(response)
            // if(response.data.login.retCode == 1){  //这行在最后需要代替下面的 if true
            // eslint-disable-next-line no-constant-condition
            if(response.data.retCode === 1){
                alert('get courses success');
                const courses = response.data.courses
                this.$router.push({name: 'CourseIndex', params: { courses }});
            }
            else {
                _this.$message({
                    message: "openSchool()failed",
                    type: 'warning',
                });
                return false
            }
        })
        .catch((response) => {
            console.log(response)
        });
//openSchool end
```

2. the backend function activate and response:\
   in the backend in `PkuWenWenbackend/PkuWenWenbackend/urls.py` you can see `path('', include('myapp.urls'))`' in `urlpatterns` \
   which means the urls defined in `PkuWenWen/myapp/urls` was used with no prepend (the `''`means the prepend is empty )\
   so let's look at `PkuWenWen/myapp/urls`
   
```python
from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('openSchool', views.openSchool),
]
```
the urlpatterns map urls to corresponding functions like `views.register` which was defined in`PkuWenWenbackend/myapp/views.py`\
lets look at them
```python
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


@csrf_exempt
def openSchool(request):
    schoolName = request.POST.get('school', '信息科学技术学院')
    courses = [ {'date': '更新于 2021-06-03 15:56:00', 'title': 'course1 from backend openSchool'}, {'date': '更新于 2021-06-03 15:56:00', 'title': 'course2 from backend openSchool'} ]
    courses = json.JSONEncoder(ensure_ascii=False).encode(courses)
    print("将courses发回前端")
    return JsonResponse({'retCode': 1, 'courses': courses})

```
you can now see the definitions, for example: please remember in the 1 part our frontend wait in the middle of openSchool.\
\
while the frontend send it's POST request to the back end and wait, the backend check it's urlpattern and decide to use the `openSchool` function defined here\
\
it makes a string in JSON format, namely `courses`, and put it inside a `JsonResponse` and return
\
please be carefull, the `JsonResponse` is soo weak that I only dare to use it in only one way, that is:\
`return JsonResponse({'key1': <number or string>, 'key2': <number or string>, ......})`\
**dont try to put something like "a list of dicts of list of list of dict..."  inside of it.**\


3. Now the backend returns and the frontend continue from the `then` statement mentioned at the end of part 1\
   it got the data that it needs and do something else\
   in this case, we redirect to the new route namely `CourseIndex` and passing `courses` as a route parameter 
   
```javascript
        })
        .then((response) => {
            console.log(response)
            // if(response.data.login.retCode == 1){  //这行在最后需要代替下面的 if true
            // eslint-disable-next-line no-constant-condition
            if(response.data.retCode === 1){
                alert('get courses success');
                const courses = response.data.courses
                this.$router.push({name: 'CourseIndex', params: { courses }});
            }
            else {
                _this.$message({
                    message: "openSchool()failed",
                    type: 'warning',
                });
                return false
            }
        })
        .catch((response) => {
            console.log(response)
        });
//openSchool end
```

that's everything about the interaction between frontend and backend.

## how to handle the params send from the former page
at the end of the part: *how front end interact with backend?* our frontend use `this.$router.push({name: 'CourseIndex', params: { courses }});` at the very end of a normal control flow\
the params sent was handled in CourseIndex.vue in the form of `this.$route.params` or `this.$route.params.courses` in different situation\
you can read it and try to understand how it works.
