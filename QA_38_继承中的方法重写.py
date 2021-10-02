# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 10:03
"""
方法重写：override
python中不存在 函数重载
"""


class Father:
    def __init__(self, first_name, blood):
        self.first_name = first_name
        self.blood = blood

    def show_name(self):
        print(self.first_name)


class Son(Father):
    def __init__(self, first_name, blood, years):
        super(Son, self).__init__(first_name, blood)
        self.years = years

    def show_name(self):
        print(self.years)


s = Son("wang", "O", "25")
s.show_name()