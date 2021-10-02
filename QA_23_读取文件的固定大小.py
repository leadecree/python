# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 08:57
from functools import partial

record_size = 32
with open("file", "rb") as f:
    r = iter(partial(f.read, record_size), b"")
    for t in r:
        pass