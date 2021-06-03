from django.db import models
import json
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


# 问题回复
class Reply(models.Model): 
    proNum = models.IntegerField() # 点赞数
    conNum = models.IntegerField() # 点踩数
    replyer = models.CharField(max_length=32) # 用户名，在后台记录，在前台匿名
    qid = models.IntegerField() #这个回复所属的问题在数据库里的id
    content = models.TextField() 

# 问题
class Question(models.Model):
    publisher = models.CharField(max_length=32, default='userName') # 提问者：用户名
    # 采用匿名提问的方式，后台记录提问者，但前台不显示提问者相关信息
    title = models.CharField(max_length=50, default='xxx')  # 提问的题目
    content = models.TextField(default = '...') # 提问的内容
    cid = models.IntegerField() # 问题所属的课程在数据库里的id


# 课程
class Course(models.Model):
    sid = models.IntegerField() # 课程所属院系
    course_id = models.CharField(max_length = 25, default = '0000') #课程号
    course_name = models.TextField(max_length = 25) #课程名


# 院系
class School(models.Model):
    school_name = models.CharField(max_length = 30) #院系名
