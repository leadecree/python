# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/23 0023 07:05
"""
这是一个属性访问截断器，即在你访问属性时，这个方法会把你的访问行为截断，并优先执行此方法中的代码，此方法应该是属性查找顺序中优先级最高的。

属性查找顺序：
实例的getattribute-->实例对象字典-->实例所在类字典-->实例所在类的父类(MRO顺序）字典-->实例所在类的getattr-->报错
"""


class People:
    a = 200


class Student(People):
    a = 100

    def __init__(self, a):
        self.a = a

    def __getattr__(self, item):
        print('没有找到:', item)

    def __getattribute__(self, item):
        print('属性访问截断器')
        if item == 'a':
            return 1
        return super().__getattribute__(item)


stu = Student(1)
print(stu.a)  # 输出结果为：1