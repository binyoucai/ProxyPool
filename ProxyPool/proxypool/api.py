#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 接口模块
@Time    : 2018/7/28 上午9:42
@Author  : 北冥神君
@File    : api.py
@Software: PyCharm
"""


from flask import Flask, g

from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>欢迎使用代理池</h2>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()