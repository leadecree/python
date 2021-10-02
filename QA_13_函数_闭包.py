# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 10:34

# 闭包：python允许在函数的内部再定义新的函数形成函数的嵌套定义,
# 在一个内部函数中，对外部作用域的变量进行引用，
# (并且一般外部函数的返回值为内部函数)，那么内部函数就被认为是闭包
"""
def outer_func(x):
    y = 10

    def inner_func():
        print(x + y)

    return inner_func


r = outer_func(3777)
r()


"""
"""
def outer_func(x):
    y = 10
    def inner_func():
        nonlocal y
        y = 50
        print(x + y)
    return inner_func

r = outer_func(20)
r()

"""


def outer_func(x):
    y = [1, 2, 3]

    def inner_func():
        y.append(x)
        print(y)

    return inner_func


r = outer_func(20)
r()
