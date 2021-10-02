# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/21 0021 17:32

# def定义的函数内使用yield关键字，调用的结果就是生成器，这个函数也不再是一个函数了


# 1  yield和return的区别:
"""
yield:暂停，下次重yield语句继续执行
return：结束

"""
""" """


def yield_func1():
    for i in range(3):
        yield i


for x in yield_func1():
    print(x)


# 2 通过send从外部传值给生成器内部传值： send 相当于next
# 使用send传值要先启动一次生成器，否则失败
def yield_func2():
    y = yield 10
    print(y)


g = yield_func2()
print(next(g))  # 10
g.send(100)


# 3 生成器的作用是节约内存，特别是读取大文件时。
with open("./data.txt", 'r', encoding="utf-8") as f:
    context = f.readlines()
    for line in context:
        print(line)


