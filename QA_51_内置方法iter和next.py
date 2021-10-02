# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 16:29
"""
迭代器：__iter__ __next__
"""


class MyIterator(object):
    def __iter__(self):
        return self

    def __next__(self):
        return 123
