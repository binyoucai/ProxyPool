#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 错误处理
@Time    : 2018/7/24 上午7:18
@Author  : 北冥神君
@File    : error.py
@Software: PyCharm
"""

class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯竭')
