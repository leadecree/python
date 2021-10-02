# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/22 0022 08:59

"""
在程序执行时创建一个临时文件或目录，并希望使用完之后可以自动销毁掉。
"""
from tempfile import TemporaryFile
with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')
    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()