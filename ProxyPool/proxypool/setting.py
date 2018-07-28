#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 全局变量配置模块 db.py, getter.py, tester.py, scheduler.py
@Author  : 北冥神君
@File    : setting.py
@Software: PyCharm
"""


# ———————————————————————————————————————————华丽分割线——————————————————————————————————————————————————————————————————
# db.py模块全局变量 REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY, MAX_SCORE, MIN_SCORE, INITIAL_SCORE
# Redis配置
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'
# 代理分数配置
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# ———————————————————————————————————————————华丽分割线——————————————————————————————————————————————————————————————————

# getter.py 全局变量 POOL_UPPER_THRESHOLD
# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# ———————————————————————————————————————————华丽分割线——————————————————————————————————————————————————————————————————

# tester.py全局变量  TEST_URL, VALID_STATUS_CODES, BATCH_TEST_SIZE

# 代理ip测试站点，建议抓哪个网站填那个
TEST_URL = 'http://www.baidu.com'
# 测试响应状态码
VALID_STATUS_CODES = [200, 302]
# 最大批测试量
BATCH_TEST_SIZE = 10

# ———————————————————————————————————————————华丽分割线——————————————————————————————————————————————————————————————————

# scheduler.py 全局变量 TESTER_CYCLE, GETTER_CYCLE, API_HOST, API_PORT, TESTER_ENABLED, GETTER_ENABLED, API_ENABLED
# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300
# web API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 测试器、获取器、api接口 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# ———————————————————————————————————————————华丽分割线——————————————————————————————————————————————————————————————————
