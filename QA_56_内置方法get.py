# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/23 0023 07:19
"""
一个描述器就是一个实现了三个核心的属性访问操作(get, set, delete) 的类，分别
为__get__() 、__set__() 和__delete__() 这三个特殊的方法。这些方法接受一个实
例作为输入，之后相应的操作实例底层的字典。
"""


class Integer(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


"""
为了使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中
"""


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x)
print(p.y)

# 触发__get__
print(Point.x.name)

# 触发__set__
Point.x.name = "hello"
print(Point.x.name)

# 触发__delete__
del Point.x.name