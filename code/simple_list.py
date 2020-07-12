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

vtubers = ['miko', 'watame', 'fubuki', 'pekora']
print([name for name in vtubers if len(name) > 5])