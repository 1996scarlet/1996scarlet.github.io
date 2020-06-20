from functools import lru_cache


class BaseHashTable():
    def __init__(self, *, init_size=16,
                 hash_func=None,
                 loader_factor=0.75):
        self._size = init_size
        self._loader_factor = loader_factor
        self._hash_func = hash_func if hash_func else hash
        self._create()

    def _create(self):
        self._rehash_thd = int(self._size * self._loader_factor)
        self._entry = [[] for i in range(self._size)]
        self._filled = 0

    @lru_cache
    def _hash(self, key):
        # 0x7FFFFFFF
        hashed = self._hash_func(key)
        # 等价于 hashed % self._size
        return self._size - 1 & hashed

    def _rehash(self):
        raise NotImplementedError

    def _insert(self, key, value):
        raise NotImplementedError

    def _search(self, key):
        raise NotImplementedError

    def _delete(self, key):
        raise NotImplementedError

    # value = ht["key"]
    def __getitem__(self, key):
        return self._search(key)

    # ht["key"] = value
    def __setitem__(self, key, value):
        self._insert(key, value)
    
        if self._filled > self._rehash_thd:
            self._size <<= 1
            self._rehash()

    # del ht["key"]
    def __delitem__(self, key):
        self._delete(key)


class HashTable(BaseHashTable):

    def _insert(self, key, value):
        # 获取key对应的哈希值
        index = self._hash(key)
        # 根据哈希值获得对应的链表索引
        index_list = self._entry[index]

        if not index_list:
            self._filled += 1

        # 如果该key已经存在就更新value
        for i, item in enumerate(index_list):
            if item[0] == key:
                index_list[i] = (key, value)
                return

        # 如果该key不存在就新增(key, value)元组
        index_list.append((key, value))

    def _entry_reduce(self, iterable):
        for each in iterable:
            if isinstance(each, list):
                yield from self._entry_reduce(each)
            else:
                yield each

    def _rehash(self):
        reduced = self._entry_reduce(self._entry)
        self._create()

        for i in reduced:
            self._insert(*i)

        print("rehash done")

    def _search(self, key):
        index = self._hash(key)
        index_list = self._entry[index]

        for item in index_list:
            if item[0] == key:
                return item

        raise KeyError

    def _delete(self, key):
        index = self._hash(key)
        index_list = self._entry[index]

        for item in self._entry[index]:
            if item[0] == key:
                index_list.remove(item)
                if not index_list:
                    self._filled -= 1
                return

        raise KeyError

    def __repr__(self):
        reduced = self._entry_reduce(self._entry)
        return str(list(reduced))

    def __len__(self):
        return self._filled


def main_test():
    def id_hash(key):
        return key if isinstance(key, int) else id(key)

    ht = HashTable(hash_func=id_hash)

    ht["abc"] = 9
    ht[-7] = 3
    ht[-7] = 6
    ht[3] = 3
    ht[3] = "poi"

    del ht[3]
    del ht[-7]

    print(ht, ht["abc"], len(ht))


if __name__ == "__main__":
    main_test()
