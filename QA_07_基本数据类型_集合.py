# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 09:00

# 集合：无序不重复的
set_0 = {1, 2, 3, 4, 5, 5.0}
print(set_0)
# 集合的运算
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
# 交集
print(set_1 & set_2)
# 并集
print(set_1 | set_2)
# 差集
print(set_1 - set_2)
# 判断子集
set_1.issubset(set_2)
# 判断父集
set_1.issuperset(set_2)
