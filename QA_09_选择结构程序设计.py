# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 09:16

# 选择结构：使用if语句
x = input("输入一个数字： ")
x = float(x)
if x <= 10:
    print("x<=10")
elif x <= 100:
    print("10<x<=100")
elif x <= 1000:
    print("10<x<=100")
else:
    print("x>1000")
