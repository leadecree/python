# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 16:15
"""
__call__方法提供给对象可以被执行的能力，就像函数那样，而本质上，函数就是对象，函数就是一个拥有__call__方法的对象。

"""


class Stu(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return 123


s = Stu(555, 666)
r = s()
print(r)
