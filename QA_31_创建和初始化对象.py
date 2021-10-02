# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 09:28


class Company(object):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, salary, staffs, address, business):
        self.salary = salary
        self.staffs = staffs
        self.address = address
        self.business = business

    def __str__(self):
        return self.business

    def main_business(self):
        print("robots", self.business)


"""
__new__是在一个对象实例化的时候所调用的第一个方法，在调用__init__初始化前，先调用__new__。
__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由 Python 解释器自动提供，后面的参数直接传递给__init__。
__new__对当前类进行了实例化，并将实例返回，传给__init__的self。但是，执行了__new__，并不一定会进入__init__，只有__new__返回了当前类cls的实例，当前类的__init__才会进入。
若__new__没有正确返回当前类cls的实例，那__init__是不会被调用的，即使是父类的实例也不行，将没有__init__被调用。
__new__方法主要是当你继承一些不可变的 class 时（比如int, str, tuple）， 提供给你一个自定义这些类的实例化过程的途径


__init__(self, )此方法为类的初始化方法。当构造函数被调用的时候的任何参数都将会传给它。
"""

tx = Company(10, 10000, "深圳", "game")
print(tx)