from django.db import models


# Create your models here.

class ServerInfo(models.Model):
    """
    收集物理物理设备信息
    """
    server_types = {
        (0, 'PC服务器'),
        (1, '刀片服务器'),
        (2, '小型机'),
        (3, '未知'),
    }
    created_types = {
        ('auto', '自动添加'),
        ('manual', '手动添加'),
    }
    server_type = models.SmallIntegerField(choices=server_types, default=0, verbose_name="服务器类型")
    created_type = models.CharField(choices=created_types, max_length=32, default='auto', verbose_name="添加方式")
    # hosted_on = models.ForeignKey('self', related_name='hosted_on_server', blank=True, null=True, verbose_name="宿主机",
    #                               on_delete=models.CASCADE)
    ipv4_add = models.CharField(max_length=30, default='', verbose_name="IPv4地址")
    mac_add = models.CharField(max_length=200, default='', verbose_name="MAC地址")
    model_type = models.CharField(max_length=120, null=True, blank=True, verbose_name="服务器型号")
    host_name = models.CharField(max_length=120, null=True, blank=True, verbose_name="主机名")
    os_type = models.CharField(max_length=64, null=True, blank=True, verbose_name="操作系统类型")
    os_distribution = models.CharField(max_length=64, null=True, blank=True, verbose_name="系统发行商")
    os_release = models.CharField(max_length=64, null=True, blank=True, verbose_name="操作系统版本")

    def __str__(self):
        return '%s-%s' % (self.id, self.host_name)

    class Meta():
        verbose_name = "服务器"
        verbose_name_plural = "服务器"
