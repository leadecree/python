# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/23 0023 07:37
# 使用面向对象的方法实现线程
"""
重写run方法
"""


import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(10):
            print("-------test-----------")


def test():
    t = MyThread()
    t.start()


test()