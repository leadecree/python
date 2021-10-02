# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 16:32
"""
当实例对象通过[]运算符取值时，会调用它的方法getitem。
"""


class DataBase:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.d = {self.id: 1,
                  self.address: "0.0.0.0",
                  }

    def __getitem__(self, key):
        return self.d.get(key, "default")


data = DataBase(1, "0.0.0.0")
print(data["hi"])
print(data[data.id])

"""
在用 for..in.. 迭代对象时，如果对象没有实现 __iter__ __next__ 迭代器协议，Python的解释器就会去寻找__getitem__来迭代对象，
"""


class Animal:
    def __init__(self, animal_list):
        self.animals_name = animal_list

    def __getitem__(self, index):
        return self.animals_name[index]


animals = Animal(['dog', 'car', 'fish'])

for animal in animals:
    print(animal)
