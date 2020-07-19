# import sys

# print(sys.getrefcount('mea'))
# vtuber = ['mea', 'aqua', 'alice']
# print(sys.getrefcount('mea'))

# mea, aqua, alice = 'mea', 'aqua', 'alice'
# print(sys.getrefcount('mea'))
# vup = [mea, aqua, alice]
# print(sys.getrefcount('mea'))

# print(list(map(lambda x, y: x is y, vtuber, vup)))

# d0 = 3.14
# d1 = 3.14
# print(d0 is d1)

# s0 = "a@be#ee"
# s1 = "a@be#ee"
# print(s0 is s1)

# r0, r1 = range(5), range(5)
# # 二者指向了不同的对象
# print(r0 is r1)  # False

# r2 = r0
# # 二者是相同对象的引用
# print(r0 is r2)  # True

# from matplotlib import pyplot as plt
# import sys

# sizes = []
# for i in range(2**5):
#     sizes.append(sys.getsizeof(sizes))

# print(sizes)
# plt.plot(sizes)
# plt.show()

'''
res = [[]]

for num in range(3):
    res += [r + [num] for r in res]

print(res)
'''

# nums = range(3)

# print(
#     [(x, y, z)
#     for x in nums
#     for y in nums
#     for z in nums
#     if x != y != z]
# )

# vtubers = ['miko', 'watame', 'fubuki', 'pekora']
# print([name for name in vtubers if len(name) > 5])

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# print(fib(0))

# def func(name, comp='hololive', *args, **kwargs):
#     return comp, name, kwargs

# print(func('aqua', age=5))
# print(func('alice', comp='2434', age=16))

# def wrap(*args, **kwargs):
#     print(args)
#     print(kwargs)

# wrap('mea', 18, types='debu')

# def func(var1, *args, **kwargs):
#     return var1, args, kwargs

# print(func(*range(5), poi='poi'))
# print(func(1, poi='poi'))

# print(func(1, 2, default=-1, poi='poi'))

# def recv(maxsize, tag='socket', *, block):
#     return maxsize, tag, block

# print(recv(1024, block=True))
# print(recv(4096, 'files', block=True))

# from collections import namedtuple

# Vtuber = namedtuple('Vtuber', ['name', 'age', 'company'])

# mea = Vtuber('mea', 18, None)

# print(mea[0] is mea.name)
# print(mea)

# a = Vtuber()
# print(a.name)

# t = (1, 2, [30, 40])

# try:
#     t[2] += [50, 60]
# except TypeError as e:
#     print(e)

# print(t)
class MySeq:
    def __getitem__(self, index):
        if isinstance(index, slice):
            print(f"slice: {index}")
        elif isinstance(index, int):
            print(f"index: {index}")
        else:
            msg = f"{type(self)} indices must be integers"
            raise TypeError(msg)

s = MySeq()

s[9]
s[::-1]
s["key"]