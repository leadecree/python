# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 08:57
import gzip
import bz2

with gzip.open("file.gz", "rt") as f:
    t1 = f.readlines()

with bz2.open("file.gz", "rt") as f:
    t2 = f.readlines()