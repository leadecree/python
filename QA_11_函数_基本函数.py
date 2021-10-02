# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/19 0019 09:46
# 函数：使用def 定义


def basic(x, y, z):
    if x <= y:
        if y <= z:
            return z, y, x

        else:
            if x <= z:
                return y, z, x
            else:
                return y, x, z
    else:
        if x <= z:
            return z, x, y
        else:
            if y <= z:
                return x, z, y
            else:
                return x, y, z


def default_func(x, y, z, flag=True):
    while flag:
        for i, j, k in zip(x, y, z):
            if i == j == k:
                print(i, j, k)
                flag = False


def locate_params(*args):
    x, *y = args
    print(x, y)


def keys_params(**kwargs):
    print(kwargs)


def random_len_default_func(f, *args, flag=True, **kwargs):
    print(f, args, flag, kwargs)
    for i in args:
        if flag is True:
            f += i
        else:
            f += kwargs["year"]
            return f
    return f


if __name__ == '__main__':
    a, b, c = basic(6, 9, 3)
    m, n, t = [1, 2, 3, 4, 5], [2, 3, 1, 4, 6], [3, 2, 1, 4, 7]

    default_func(m, n, t)
    locate_params(1, 2, 3, 4)
    keys_params(name="python", year=2000)

    r_f = random_len_default_func(0, 1, 2, 3,4, flag=True, name="python", year=2000)
    print(r_f)