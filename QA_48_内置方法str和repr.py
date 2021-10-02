# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 10:48
"""
两者的目的都是为了显式的显示对象的一些必要信息，方便查看和调试。
__str__被print默认调用，__repr__被控制台输出时默认调用。
即，使用__str__控制用户展示，使用__repr__控制调试展示。
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s" % self.name

    def __repr__(self):
        return "%s,%d" % (self.name, self.age)


stu = Student('zlw', 26)
print(str(stu))
print(repr(stu))
