from django.db import models

class User(models.Model):
    account = models.CharField('账号',max_length=20)
    password = models.CharField('密码',max_length=20)
    phone = models.CharField('电话',max_length=11,blank=True)
    email = models.CharField('邮箱',max_length=30,blank=True)
    nickName = models.CharField('昵称',max_length=20)
    introduc = models.CharField('简介',max_length=256,blank=True)
    createDate = models.DateTimeField('创建日期',auto_now_add=True)
    editDate = models.DateTimeField('修改日期',auto_now=True)
    token = models.CharField('token',max_length=256,blank=True)
    pushToken = models.CharField('推送token',max_length=256,blank=True)


