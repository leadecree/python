# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 10:10

"""
Python中的类提供了很多双下划线开头和结尾__xxx__的方法，这些方法是Python运行的基础，很多功能背后都是通过调用这些内置方法来实现的。
"""

class Stu(object):
    pass


print(dir(Stu))
"""
__init__、
__new__、
__del__、
__module__、
__class__、
__call__、
__len__、
__str__、
__repr__、
__format__
__getattr__、
__setattr__、
__delattr__、
__getattribute__、
__dir__、
__iter__、
__next__、
__enter__、
__exit__、
__doc__、        
__getitem__(self, key)、     
__setitem__(self, key, value) 、 
__delitem__(self, key)、  
__iter__(self)、     
__reversed__(self)、  
__contains__(self, item)、
"""