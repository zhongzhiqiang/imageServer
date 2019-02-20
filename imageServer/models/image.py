# coding:utf-8
# Time    : 2019/2/20 下午2:58
# Author  : Zhongzq
# File    : image.py
# Software: PyCharm
from django.db import models


class MyImage(models.Model):
    image = models.ImageField(
        u'图片'
    )
    image_desc = models.CharField(
        u'图片描述',
        max_length=100,
        default=''
    )

    @property
    def image_url(self):
        return self.image.url

    def __unicode__(self):
        return self.image.url

    class Meta:
        verbose_name = '图片存储'
        verbose_name_plural = verbose_name
