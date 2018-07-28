#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@content : 主程序入口
@Time    : 2018/7/28 上午11:02
@Author  : 北冥神君
@File    : run.py
@Software: PyCharm
"""

from proxypool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except BaseException:
        main()


if __name__ == '__main__':
    print('启动')
    print('\n'.join([''.join([('ProxyPools'[(x - y) % 10] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
        x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))
    main()
