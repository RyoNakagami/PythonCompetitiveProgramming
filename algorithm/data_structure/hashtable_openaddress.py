class OpenAdressHashTable:
    def __init__(self, hash_length: int):
        self.hash_length = hash_length
        self.bucket = [None] * self.hash_length
    
    def h1(self, key: int) -> int:
        return key % self.hash_length
    
    def h2(self, key: int) -> int:
        return 1 + (key % (self.hash_length - 1))

    def double_hash(self, key: int, i: int) -> int:
        return (self.h1(key) + i * self.h2(key)) % self.hash_length
    
    def insert(self, key: int):
        if self.search(key) is not None:
            raise ValueError("The key already exists")
        else:
            i = 0
            while True:
                idx = self.double_hash(key, i)
                if self.bucket[idx] == None:
                    self.bucket[idx] = key
                    break
                elif i >= self.hash_length:
                    raise Exception("The hash_length is not enough")
                else:
                    i += 1
    
    def search(self, key: int) -> int:
        i = 0
        while True:
            idx = self.double_hash(key, i)
            if self.bucket[idx] == key:
                return idx
            elif self.bucket[idx] == None or i >= self.hash_length:
                return None
            else:
                i += 1

    def remove(self, key: int):
        idx = self.search(key)
        if idx is None:
            raise ValueError("The key does not exists")        
        self.bucket[idx] = None 
