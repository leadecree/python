# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 11:33
# 带不定长参数的装饰器


def calculate_area(fn):
    def process(n, *args):
        if n == 2:
            print(fn(args[0], args[1]))
        elif n == 3:
            print(fn(args[0], args[1], args[2]))

    return process


@calculate_area
def right_triangle(h, w):
    return h * w / 2


right_triangle(2, 3, 4)


@calculate_area
def rectangle(h, w):
    return h * w


rectangle(2, 4, 5)


@calculate_area
def trapezoid(h, top, down):
    return (top + down) * h / 2


trapezoid(3, 2, 8, 5)
