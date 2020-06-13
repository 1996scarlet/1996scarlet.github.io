def A(n):
    yield n*n

def B(n):
    yield A(n)

print(B(5))

exit(0)

def producer(c):

    res = c.send(None)
    print(res)

    for i in range(5):
        c.send(i)
        print(f"p{i}")


def customer():
    while True:
        n = yield 0
        print(f"c{n}")

c = customer()
producer(c)

exit(0)

from greenlet import greenlet

def func1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()
    print(5)

def func2():
    print(3)
    gr1.switch()
    print(4)

gr1 = greenlet(func1)
# 设置 parent 为 gr1
# gr2 执行完毕后回到 gr1 继续执行
gr2 = greenlet(func2, gr1)

gr1.switch()

print('-'*10)

def func3():
    yield 1
    yield from func4()
    yield 2

def func4():
    yield 3
    yield 4

coro = func3()

for item in coro:
    print(item)

print('-'*10)

import asyncio

async def func5():
    print(1)
    await asyncio.sleep(2)
    print(2)

async def func6():
    print(3)
    await asyncio.sleep(2)
    print(4)

async def main():
    await asyncio.gather(
        func5(),
        func6()
    )

asyncio.run(main())

def func7():
    for x in range(5):
        yield x

for x in func7():
    print(x)