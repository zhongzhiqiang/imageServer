# coding:utf-8
# Time    : 2019/2/20 下午3:19
# Author  : Zhongzq
# File    : fabfile.py
# Software: PyCharm
from fabric.api import (local, cd, run, hosts, with_settings)

HOST_IP = '132.232.16.7'
HOST_USER = 'ubuntu'


@hosts(HOST_IP)
@with_settings(user=HOST_USER)
def deploy():
    with cd('/data/imageServer'):
        run('git pull --rebase origin master')
        run('python manage.py collectstatic --no-input')
        run('python manage.py migrate')
        run('touch ./uwsgi.ini')
