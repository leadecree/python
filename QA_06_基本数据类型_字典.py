# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 08:45

# 1 字典：键值对的形式  key:value
dict_x = {"name": "python", "year": 1994}
dict_y = dict()  # 空字典

# 2 字典元素的访问:通过键获取值
x, y = dict_x["name"], dict_x["year"]
print(x, y)

# 3 获取全部的key 或者 value
keys, values, k_v = dict_x.keys(), dict_x.values(), dict_x.items()
print(keys, values, k_v)
