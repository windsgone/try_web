#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import *				# 导入时间模块
from sys import argv				# 导入系统模块

script, filename = argv				# 将文本名作为参数传递给程序

data_list = ['曹国伟','许良杰','杜红','褚达晨','陈彤','张宸阳','余正钧','王雅娟','王高飞',
			'葛景栋','彭少彬','推广微博','微博营销','信息流广告','微博橱窗','微博广告',
			'微博商业化','粉丝通','微任务','微博商业平台','到店宝','微博自助广告平台',
			'新浪微博','微博开放平台','微博社区委员会','微博辟谣','微博实名制','微博社区公约',
			'微博生态圈','微博基金','微博开发者基金','自媒体协会','微博客户端',
			'微博桌面','智能排序','天气通','微博阅读数','新浪视野','媒体版微博']

now = date.today()					# 将日期赋予now

target = open(filename, "w")		# 打开可写入的文本

for name in data_list:
	target.write('http://s.weibo.com/weibo/' + name + '&xsort=hot&timescope=custom:' 
		+ str(now) + ':' + str(now) + '&Refer=g' + '\n')
									# 循环写入地址
target.close()						# 关闭文本