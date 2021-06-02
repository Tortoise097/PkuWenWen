from django.db import models

# Create your models here.
class Note(models.Model):
    note = models.CharField(max_length=180)

class UserModel(models.Model):
    userName = models.CharField(max_length=32, default='userName')  # 用户名
    password = models.CharField(max_length=50, default='000000')  # 密码
    major = models.CharField(max_length=20, default='undefined')  # 专业
    email = models.CharField(max_length=50, default='emailaddress')  # 电子邮件
    phoneNumber = models.CharField(max_length=32, default='phonenumber')  # 电话号码

    def __str__(self):
        return self.userName

        