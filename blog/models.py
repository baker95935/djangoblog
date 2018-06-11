from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)  # 博客标题
    body = models.TextField()                   # 博客正文
    timestamp = models.DateTimeField()          # 创建时间

class Member(models.Model):
    username = models.CharField(max_length=60)  #用户名
    password = models.CharField(max_length=32)  #密码
    timestamp = models.DateTimeField() #创建时间

class Link(models.Model):
    title = models.CharField(max_length = 60) #链接标题
    link = models.CharField(max_length = 120) #链接地址
    order = models.IntegerField() #排序
    timestamp = models.DateTimeField() #创建时间

class PostType(models.Model):
    title = models.CharField(max_length = 60) #分类标题
    order = models.IntegerField() #排序
    timestamp = models.DateTimeField() #创建时间
