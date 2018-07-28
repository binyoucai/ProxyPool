#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 手动导入模块
@Time    : 2018/7/28 上午10:57
@Author  : 北冥神君
@File    : importer.py
@Software: PyCharm
"""

from proxypool.db import RedisClient

conn = RedisClient()


def set(proxy):
    result = conn.add(proxy)
    print(proxy)
    print('录入成功' if result else '录入失败')


def scan():
    print('请输入代理, 输入exit退出读入')
    while True:
        proxy = input()
        if proxy == 'exit':
            break
        set(proxy)


if __name__ == '__main__':
    scan()
