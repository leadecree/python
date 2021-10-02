# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/23 0023 07:43
# 5 进程池

from multiprocessing import Pool


def worker(num):
    print(num)


def main():
    pool = Pool(3)

    for i in range(10):
        pool.apply_async(worker, args=(i,))

    print("----------开始--------------")
    pool.close()
    # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool, join函数等待所有子进程结束
    pool.join()
    print("----------结束--------------")


if __name__ == '__main__':
    main()