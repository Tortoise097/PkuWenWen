from djongo import models

# Create your models here.
'''
用户类
说明：登录和注册需要的是email和password
用户名唯一。
发帖的时候可以匿名也可以显示自己的名字，专业（major）同理。
如果不匿名，发帖时会显示用户名&专业，
反之这两项会随机生成
'''
class User(models.Model):
    userName = models.CharField(max_length=30)  
    password = models.CharField(max_length=32)
    major = models.CharField(max_length=32)
    email = models.CharField(max_length=50)