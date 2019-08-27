# -*- coding: utf-8 -*-
import locale
import sys
import urllib
import os
import time

try:
    get = [sys.argv[1], sys.argv[2], sys.argv[3]]
except IndexError:
    sys.exit('参数错误')
if get[0] == 'create' and get[1] == 'post':
    file = open('./' + get[2] + '.md', 'w')
    file.write('---\n')
    title = input('what\'s the title of this post\n')
    categories = input('what\'s the categories of this post\n')
    file.write('title: ' + title + '\n')
    file.write('date: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
    file.write('categories: ' + categories + '\n')
    file.write('---\n')
