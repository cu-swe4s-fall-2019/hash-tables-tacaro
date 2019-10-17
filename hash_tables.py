import hash_functions
import numpy as np


class LinearProbe:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.table = [None] * N

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        hash_slot = start_hash
        if self.table[start_hash] is None:  # base case
            self.table[start_hash] = (key, value)
        else:
            for i in range(self.N):
                query = (hash_slot + i) % self.N
                if self.table[query] is None:
                    self.table[query] = (key, value)
                    return True
            return False  # executes if key not found

        # pass

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        for i in range(self.N):
            query = (start_hash + i) % self.N
            if self.table[query][0] == key:
                return self.table[start_hash][1]  # return the value, index 1
            if self.table[start_hash] is None:
                return None
        return None  # executes if key not found


class ChainedHash:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N
        self.table = [[]]*N  # create emtpy list of lists with N elements

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        for i in range(self.N):
            query = (start_hash + i) % self.N
            if self.table[query] is None:
                self.table[query] = (key, value)
                return True
        return False

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        for i in range(self.N):
            query = (start_hash + i) % self.N
            if self.T[query] is None:
                return None
            if self.T[query][0] == key:
                return self.T[query][1]
