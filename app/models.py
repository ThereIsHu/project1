from django.db import models

# Create your models here.
class userinfo( models.Model):
    # 姓名 str类型，verbose_name 是后台管理界面中显示的内容
    name = models.CharField(max_length=20, verbose_name='用户账号')
    # 年龄 int型
    password = models.CharField(max_length=20, verbose_name='用户密码')

class admin( models.Model):
    # 姓名 str类型，verbose_name 是后台管理界面中显示的内容
    name = models.CharField(max_length=20, verbose_name='管理员账号')
    # 年龄 int型
    password = models.CharField(max_length=20, verbose_name='管理员密码')

class login( models.Model):
    ip = models.CharField(max_length=20, verbose_name='ip地址')
    browserType = models.CharField(max_length=20, verbose_name='浏览器类型')

class answer( models.Model):
    key = models.CharField(max_length=20, verbose_name='关键字')
    text = models.CharField(max_length=20, verbose_name='文本')
    picture = models.CharField(max_length=20, verbose_name='图片')
    url = models.CharField(max_length=20, verbose_name='链接')

class words (models.Model):
    word = models.CharField(max_length=1000, verbose_name='词频')
    times = models.TimeField(verbose_name='时间')