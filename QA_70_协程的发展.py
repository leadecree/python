# *_* coding:utf-8 *_*
# @author:sdh
# @Time : 2021/9/23 0023 08:13
"""
Python中的协程经历了很长的一段发展历程。其大概经历了如下三个阶段：
(1) 最初的生成器变形yield/send 引入
(2) @asyncio.coroutine和yield from *
(3) 引入async/await关键字
"""

# yield + send（利用生成器实现协程）
"""
生产者-消费者”模型来看一下协程的应用，生产者生产消息后，
直接通过yield跳转到消费者开始执行，
待消费者执行完毕后，切换回生产者继续生产
"""


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER]Consuming %s...' % n)
        r = '200 OK'


def producer(c):
    # 启动生成器
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER]Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER]Consumer return: %s' % r)
    c.close()


# asyncio + yield from 实现协程
"""
asyncio是Python3.4版本引入的标准库，直接内置了对异步IO的支持。
asyncio的异步操作，需要在coroutine中通过yield from完成。
"""
import asyncio


@asyncio.coroutine
def test(i):
    print('test_1', i)
    r = yield from asyncio.sleep(1)
    print('test_2', i)


# asyncio + async/await
"""
为了简化并更好地标识异步IO，从Python3.5开始引入了新的语法async和await，
可以让coroutine的代码更简洁易读。
请注意，async和await是coroutine的新语法，使用新语法只需要做两步简单的替换：
(1) 把@asyncio.coroutine替换为async
(2) 把yield from替换为await
"""


async def test1(i):
    print('test_1', i)
    await asyncio.sleep(1)
    print('test_2', i)


if __name__ == '__main__':

    c = consumer()
    producer(c)

    loop = asyncio.get_event_loop()
    tasks = [test(i) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    loop = asyncio.get_event_loop()
    tasks = [test1(i) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
