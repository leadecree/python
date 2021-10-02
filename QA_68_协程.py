# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/23 0023 07:57
"""
协程，又称作Coroutine。从字面上来理解，即协同运行的例程，它是比线程（thread）更细量级的用户态线程，
特点是允许用户的主动调用和主动退出，
挂起当前的例程然后返回值或去执行其他任务，接着返回原来停下的点继续执行。
等下，这是否有点奇怪？我们都知道一般函数都是线性执行的，不可能说执行到一半返回，等会儿又跑到原来的地方继续执行。
但一些熟悉python（or其他动态语言）的童鞋都知道这可以做到，答案是用yield语句。

其实这里操作系统具有getcontext和swapcontext这些特性，通过系统调用，可以把上下文和状态保存起来，切换到其他的上下文，
这些特性为coroutine的实现提供了底层的基础。
"""

# 7 python实现协程
# 最简单的协程实现 gevent

"""
gevent是第三方库，通过greenlet实现协程，其基本思想是：
当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，
再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，
有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，
这一过程在启动时通过monkey patch完成.
"""

"""
Python中解决IO密集型任务（打开多个网站）的方式有很多种，比如多进程、多线程。但理论上一台电脑中的线程数、进程数是有限的，
而且进程、线程之间的切换也比较浪费时间。所以就出现了“协程”的概念。协程允许一个执行过程A中断，然后转到执行过程B，在适当的时候再一次转回来，有点类似于多线程。但协程有以下2个优势：
协程的数量理论上可以是无限个，而且没有线程之间的切换动作，执行效率比线程高。
协程不需要“锁”机制，即不需要lock和release过程，因为所有的协程都在一个线程中。
相对于线程，协程更容易调试debug，因为所有的代码是顺序执行的。
"""

from gevent import monkey
import gevent
import random
import time

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())


gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
])