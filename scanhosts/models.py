from django.db import models


# Create your models here.
class UserIPInfo(models.Model):
    ipv4_address = models.CharField(max_length=40, default='', verbose_name=u'ipv4地址', null=True)
    update_time = models.DateTimeField(verbose_name=u"更新时间", auto_now=True)

    class Meta:
        verbose_name = u'用户访问地址信息表'
        verbose_name_plural = verbose_name
        db_table = "user_ip_info"


class BrowseInfo(models.Model):
    useragent = models.CharField(max_length=100, default='', verbose_name=u"用户浏览器agent信息", null=True)
    blk_id = models.CharField(max_length=256, verbose_name=u"唯一设备ID", default="")
    user_ip = models.ForeignKey("UserIPInfo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"用户浏览器信息表"
        verbose_name_plural = verbose_name
        db_table = "browse_info"
