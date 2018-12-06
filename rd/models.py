from django.db import models

# Create your models here.

# 基础配置的参数
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


# 系统用户，包括普通用户，后台用户，领导用户等。
class BUser(models.Model):
    name = models.CharField(max_length=255, verbose_name='姓名', null=True, blank=True)
    account = models.CharField(max_length=255, verbose_name='账号', null=True, blank=True)
    # 需要加密
    passwrod = models.CharField(max_length=255, verbose_name='密码', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='电话', null=True, blank=True)
    email = models.CharField(max_length=255, verbose_name='', null=True, blank=True)
    type = models.IntegerField(verbose_name='用户类型', default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "系统用户"
        verbose_name_plural = verbose_name


# 领导名册类型
class BUserListType(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='类型名称')
    type = models.ForeignKey('BUserListType', null=True, blank=True, verbose_name="父类名称",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "领导名册类型"
        verbose_name_plural = verbose_name


class BMessageType(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='留言类型')
    # 设计父级类型，可以实现无限深度的类型分类
    type = models.ForeignKey('BMessageType', null=True, blank=True, verbose_name='父级类型', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "留言类型"
        verbose_name_plural = verbose_name


class BMessage(models.Model):
    user = models.ForeignKey(BUser, verbose_name='留言人',null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, verbose_name='留言标题', null=True, blank=True)
    content = models.TextField(verbose_name='留言内容', null=True, blank=True)
    settime = models.DateTimeField(verbose_name='留言时间', null=True, blank=True)
    ipaddress = models.CharField(max_length=255, null=True, blank=True, verbose_name='ip地址')
    type = models.ForeignKey(BMessageType, verbose_name="留言类型", null=True,  on_delete=models.SET_NULL)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "群众留言"
        verbose_name_plural = verbose_name


