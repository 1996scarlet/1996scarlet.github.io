# from bintrees import FastRBTree


# def hash_builder(size=0xffffffff):
#     # 0xffffffff = 2**32 - 1
#     def hash_func(x):
#         return size & hash(x)
#     return hash_func


# def gen_hashed_ip(hash_func, addresses):
#     for ip in addresses:
#         yield hash_func(ip), ip


# # 解决偏置
# ip_list = [
#     '10.41.0.101-Real',
#     '10.41.0.101-Fake-A',
#     '10.41.0.101-Fake-B',
#     '10.41.0.102-Real',
#     '10.41.0.102-Fake-A',
#     '10.41.0.102-Fake-B',
#     '10.41.0.103-Real',
#     '10.41.0.103-Fake-A',
#     '10.41.0.103-Fake-B',
# ]

# my_hash = hash_builder()

# rbtree = FastRBTree(gen_hashed_ip(my_hash, ip_list))
# # print(rbtree)

# hashed = my_hash('a.jpg')

# try:
#     item = next(rbtree[hashed:].items())
#     print(hashed, item)
# except StopIteration:
#     print('闭环')
#     print(hashed, rbtree.min_item())

import collections
import re

def mostCommonWord(paragraph: str, banned) -> str:
    np = filter(lambda x: x, re.split("[!?',;. ]", paragraph.lower()))
    s = set(banned)
    d = list(collections.Counter(np).items())
    d.sort(key=lambda x: x[1], reverse=True)
    print(d)
    for k, v in d:
        if k not in s:
            return k

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(mostCommonWord(paragraph, banned))