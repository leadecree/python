# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 08:36

# 1 元组:元素类型可以是任意的.
tuple_a = (3, 5.5, "py")
print(tuple_a)

# 2 元组拆包
x, y, z = tuple_a
print(x, y, z)  # x, y, z = 3, 5.5, "py"

a, *b = tuple_a
print(a, b)  # a, b = 3，[5.5, 'py']

tuple_b = (1, 2, (3, 4))
m, n, (i, j) = tuple_b
print(m, n, i, j)

tuple_c = (3, 5, 7)
t, _, _ = tuple_c
print(t)

# 3 元组的切片和排序(同 字符串和列表)
