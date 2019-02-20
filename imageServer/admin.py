# coding:utf-8
# Time    : 2019/2/20 下午2:58
# Author  : Zhongzq
# File    : admin.py
# Software: PyCharm

from imageServer.models import MyImage

from django.contrib import admin


class MyImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'image_url'
    )

admin.site.register(MyImage, MyImageAdmin)
