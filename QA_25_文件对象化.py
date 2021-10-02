# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 09:01
"""
问题
需要将一个Python对象序列化为一个字节流，以便将它保存到一个文件、存储
到数据库或者通过网络传输它。

解决方案
对于序列化最普遍的做法就是使用pickle模块。
"""
import pickle
data = " "
f = open("./data.txt","wb")
pickle.dump(data,f)

"""
为了将一个对象转储为一个字符串，可以使用pickle.dumps()
"""
s = pickle.dumps(data)

"""
为了从字节流中恢复一个对象，使用pickle.load() 或pickle.loads() 函数
"""
f = open("./data.txt","rb")
data = pickle.load(f)

data2 = pickle.loads(f)