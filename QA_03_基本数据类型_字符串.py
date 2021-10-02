# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 08:04

# 字符串:单引号、双引号、三引号字符串

# 1 字符串的三种形式
x = 'python'
y = "python"
z = """python"""

print(x, y, z)  # python python python

# 2 字符串中有字符串
a = "this is 'python'"
print(a)  # this is 'python'

# 3 字符串的切片
b = "learn python"
print(b[:])  # 取全部的字符串learn python
print(b[0:5]) # 取部分左闭右开区间，learn
print(b[0:6:2]) # 区间内间隔取，lan
print(b[::-1])  # 字符串翻转，nohtyp nrael

