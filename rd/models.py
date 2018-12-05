from django.db import models

# Create your models here.


class BaseSetting(models.Model):
    name = models.CharField(max_length=255, verbose_name="字段说明")
    content = models.TextField(verbose_name="内容", null=True)
    addtime = models.DateTimeField(auto_now_add=True)
    changetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "基础配置"
        verbose_name_plural = verbose_name


class BUser(models.Model):
    name = models.CharField(max_length=255, verbose_name='姓名', null=True, blank=True)
    account = models.CharField(max_length=255, verbose_name='账号', null=True, blank=True)
    # 需要加密
    # passwrod = models.CharField(max_length=255, verbose_name='密码', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='电话', null=True, blank=True)
    email = models.CharField(max_length=255, verbose_name='', null=True, blank=True)
    type = models.IntegerField(verbose_name='用户类型', default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "系统用户"
        verbose_name_plural = verbose_name


class BMessage(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题', null=True, blank=True)
