# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 07:50

# 使用yield from 进行生成器的嵌套


# 1 yield和yield from的 对比

x_string = "python"
x_list = [1, 2, 3]
x_dict = {"name": "windows", "ages": 5}
x_gen = (i for i in range(4, 6))


def gen_func(*args, **kwargs):
    for item in args:
        for i in item:
            yield i


def yield_from_func(*args, **kwargs):
    for item in args:
        yield from item


for elm in gen_func(x_string, x_list, x_dict, x_gen):
    print(elm)
"""
yield from后面加上可迭代对象，它可以把可迭代对象里的每个元素一个一个的yield出来，对比yield来说代码更加简洁，结构更加清晰
"""
for elm in yield_from_func(x_string, x_list, x_dict, x_gen):
    print(elm)

# 2 当 yield from 后面加上一个生成器后，就实现了生成的嵌套:自动处理异常
"""
当然实现生成器的嵌套，并不是一定必须要使用yield from，
而是使用yield from可以让我们避免让我们自己处理各种料想不到的异常，
而让我们专注于业务代码的实现
"""


def sub_gen():
    """
    子生成器
    :return:
    """
    s = 0
    count = 0
    arg = 0
    while True:
        new_num = yield arg
        count += 1
        s += new_num
        arg = s / count


def proxy_gen():
    """
    代理生成器
    :return:
    """
    yield from sub_gen()


def main():
    """
    调用方
    :return:
    """
    cal = proxy_gen()
    print(next(cal))  # 先启动一次生成器 0
    print(cal.send(10))  # 10.0
    print(cal.send(20))  # 15.0
    print(cal.send(30))  # 20.0


if __name__ == '__main__':
    main()
