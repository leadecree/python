# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/23 0023 07:07
"""
问题:你想让你的对象支持上下文管理协议(with 语句)。
解决方案:为了让一个对象兼容with 语句，你需要实现__enter__() 和__exit__() 方法
"""
from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


"""
1:  编写上下文管理器的主要原理是你的代码会放到with 语句块中执行。当出现with
语句的时候，对象的__enter__() 方法被触发，它返回的值(如果有的话) 会被赋值给
as 声明的变量.
2:  with 语句块里面的代码开始执行。最后，__exit__() 方法被触发进行清理工作。
3:  不管with 代码块中发生什么，上面的控制流都会执行完，就算代码块中发生了异
常也是一样的,事实上，__exit__() 方法的第三个参数包含了异常类型、异常值和追
溯信息(如果有的话)。
4:  __exit__() 方法能自己决定怎样利用这个异常信息，或者忽略它并返回一个None 值。
如果__exit__() 返回True ，那么异常会被清空，就好像什么都没发生一样，with 语句后面的程序继续在正常执行。
"""
