# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/23 0023 07:03
"""
当使用obj.x = y的时候触发对象的setattr方法，当del obj.x的时候触发对象的delattr方法。
当尝试访问对象的一个不存在的属性时 obj.noexist 会触发getattr方法，getattr方法是属性查找中优先级最低的。
"""


class Student:
    def __getattr__(self, item):
        print('访问一个不存在的属性时候触发')
        return '不存在'

    def __setattr__(self, key, value):
        print('设置一个属性值的时候触发')
        # self.key = value  # 这样会无限循环
        self.__dict__[key] = value

    def __delattr__(self, item):
        print('删除一个属性的时候触发')
        if self.__dict__.get(item, None):
            del self.__dict__[item]


stu = Student()
stu.name = 'zlw'  # 设置一个属性值的时候触发
print(stu.noexit)  # 访问一个不存在的属性时候触发 , 返回'不存在'
del stu.name  # 删除一个属性的时候触发
