# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 11:26

# 1 概念
"""
可迭代对象：实现了__iter__方法的对象就是可迭代对象,就可以用for进行迭代，但是要成功进行for in遍历需要很多条件。
迭代器：实现__next__方法和__iter__方法且__iter__方法返回一个具有__next__方法的对象(这个对象可以是自己，也可以是其他类的对象)。
"""

"""
使用 for in 的原理：
(1) 判断对象是否可以迭代
(2) 在(1)成立的前提下，iter()函数得到对象的__iter__方法的返回值
(3) 这个返回值是一个迭代器:必须有__iter__和__next__方法
(4) 迭代器不断地调用__next__方法知道触发StopIteration终止

"""

from collections.abc import Iterable, Iterator


# 可迭代对象
class MyIterable(object):
    def __init__(self):
        self.n_list = list()

    def add_info(self, name):
        self.n_list.append(name)

    def __iter__(self):
        return MyIterator(self)


class MyIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.index < len(self.obj.n_list):
            r = self.obj.n_list[self.index]
            self.index += 1
            return r
        else:
            raise StopIteration


class IteratorAll(object):
    def __init__(self):
        self.n_list = list()
        self.index = 0

    def add(self, name):
        self.n_list.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index<len(self.n_list):
            r = self.n_list[self.index]
            self.index+=1
            return r
        else:
            raise StopIteration




if __name__ == '__main__':
    my_iter = MyIterable()

    print(isinstance(my_iter, Iterable))
    print(isinstance(iter(my_iter), Iterator))
    my_iter.add_info("111")
    my_iter.add_info("222")
    my_iter.add_info("333")
    my_iter.add_info("444")

    for i in my_iter:
        print(i)


    itor_all = IteratorAll()
    itor_all.add("xxxx")
    itor_all.add("yyyy")
    itor_all.add("zzzz")
    itor_all.add("tttt")

    for j in itor_all:
        print(j)

