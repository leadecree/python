# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 09:26
# 循环结构: while循环和for循环


while True:
    x = float(input("输入一个数："))
    if x > 100:
        break

a = [1, 2, 3, 4, 10, 100, 1000]
for i in a:
    if i == 4:
        continue
    elif i != 100:
        print(i)
    else:
        break
