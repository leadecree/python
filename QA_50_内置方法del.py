# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 16:26
"""
类似于析构函数
__del__用于当对象的引用计数为0时自动调用。
__del__一般出现在两个地方：1、手工使用del减少对象引用计数至0，被垃圾回收处理时调用。2、程序结束时调用。
__del__一般用于需要声明在对象被删除前需要处理的资源回收操作
"""


class Stu(object):
    def __init__(self, x):
        self.x = x

    def __del__(self):
        print("调用了__del__")


s = Stu(555555)
