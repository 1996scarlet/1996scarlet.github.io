from functools import lru_cache


class BaseHashTable():
    pass


class HashTable(BaseHashTable):

    def __init__(self, *, init_size=16, hash_func=None,
                 loader_factor=0.75):
        self._loader_factor = loader_factor
        self._create(init_size)
        self._hash_func = hash_func if hash_func else hash
        self._rehash_flag = False

    def _create(self, init_size):
        self._size = init_size
        self._entry = [[] for i in range(self._size)]

    @lru_cache
    def _hash(self, key):
        return self._hash_func(key) % self._size

    def _insert(self, key, value):
        index = self._hash(key)
        index_list = self._entry[index]

        if len(index_list) > 7:
            self._rehash_flag = True

        for i, item in enumerate(index_list):
            if item[0] == key:
                index_list[i] = (key, value)
                return True

        index_list.append((key, value))
        return True

    def _entry_reduce(self, iterable):
        for each in iterable:
            if isinstance(each, list):
                yield from self._entry_reduce(each)
            else:
                yield each

    def _rehash(self, init_size):
        reduced = self._entry_reduce(self._entry)
        self._create(init_size)

        for i in reduced:
            self._insert(*i)

        print("rehash done")

    def __repr__(self):
        reduced = self._entry_reduce(self._entry)
        return str(list(reduced))

    def __len__(self):
        reduced = self._entry_reduce(self._entry)
        return len(list(reduced))

    def _search(self, key):
        index = self._hash(key)
        index_list = self._entry[index]

        for item in self._entry[index]:
            if item[0] == key:
                return item[1]

        return None

    def __getitem__(self, key):
        if res := self._search(key):
            return res
        raise KeyError

    def __setitem__(self, key, value):
        self._insert(key, value)
        if self._rehash_flag:
            self._rehash(self._size * 2 + 1)
            self._rehash_flag = False


def id_mod_hash(key):
    return key if isinstance(key, int) else id(key)


# ht = HashTable(hash_func=id_mod_hash)
ht = HashTable()

ht["abc"] = 9
ht[-7] = 3
ht[-7] = 6
ht[3] = "poi"
ht[3] = 3

for i in range(2**16):
    ht[i] = i

# print(ht, len(ht))

# ht[6]

# p = {}

# for i in range(2**16):
#     p[f"a{i}"] = i
