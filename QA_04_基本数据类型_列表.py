# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 08:14

# 列表：内的元素可以是任意类型的，不同于其他语言

# 1 列表
list_a = [9, 3.1415, "python"]
print(list_a)

# 2 列表内元素的排序
# 当列表中的数据类型可以进行排序时使用 sorted进行排序

# print(sorted(list_a)) 不可以进行排序
list_b = [3, 5, 7, 4, 6, 8]
print(sorted(list_b))  # 从小到大排，[3, 4, 5, 6, 7, 8]
print(sorted(list_b, reverse=True))  # 从大到小排，[8, 7, 6, 5, 4, 3]

# 3 列表的切片
print(list_b[:])  # 取全部 [3, 5, 7, 4, 6, 8]
print(list_b[0:3])  # 取部分左闭右开区间 [3, 5, 7]
print(list_b[0:5:2])  # 取部分左闭右开区间 [3,7,6]
print(list_b[::-1])  # 翻转

# 从后向前,步长要设为负值
print(list_b[-1::-1])  # 翻转
print(list_b[-1:0:-2]) # 从后向前间隔取，左闭右开 [8, 4, 5]
