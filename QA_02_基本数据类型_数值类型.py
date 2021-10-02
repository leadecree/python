# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 07:52

# 数值类型:整数类型和浮点数类型

# 1 整数类型和浮点数类型示例
x = 10
y = 3.14
z = 5.9999
print(type(x))  # int
print(type(y))  # float
print(type(z))  # float

# 2 整数类型和浮点数类型相互转换
# float转为int采用去尾留整，而不是四舍五入。
print(int(y))  # 3
print(int(z))  # 5
print(float(x))  # 10.0

# 3 不同数值类型之间的运算
# int +-*int = int 加减乘都是int
# int / int = float 除法(无论能不能除尽)都是float

# int 和float运算都是float
a = 3
b = 13.578
c = 3

# int int int float
print(type(a + c), type(a - c), type(a * c), type(a / c))

# float float float float
print(type(a + b), type(a - b), type(a * b), type(a / b))
