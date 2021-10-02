# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 10:14
"""
__new__方法是真正的类构造方法，用于产生实例化对象（空属性）。
重写__new__方法可以控制对象的产生过程。
__init__方法是初始化方法，负责对实例化对象进行属性值初始化，此方法必须返回None，__new__方法必须返回一个对象。
重写__init__方法可以控制对象的初始化过程。
"""


# 单例模式：一个类只能有一个对象
class SingleTon(object):
    __flag = None
    __limit = True

    def __new__(cls, *args, **kwargs):
        if cls.__flag is None:
            cls.__flag = super().__new__(cls)

        return cls.__flag

    def __init__(self, name, age):
        if self.__limit is True:
            self.name = name
            self.age = age
            self.__limit = False

    def __str__(self):
        return self.name, self.age


a = SingleTon(1, 2)
print(a.name)

b = SingleTon(3, 4)
print(b.name)
