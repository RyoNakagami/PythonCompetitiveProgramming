class ConsistentHash:
    def __init__(self, server_list: list, max_hashsize: int = 100):
        self.nodes = set(server_list)
        self.max_hashsize = max_hashsize
        self._generate_hashring()

    def add_server(self, server: list):
        self.nodes |= set(server)
        self._generate_hashring()
    
    def remove_server(self, server: list):
        self.nodes -= set(server)
        self._generate_hashring()
    
    def hash_func(self, key: str):
        return hash(key) % self.max_hashsize
    
    def _generate_hashring(self):
        hash_val = list(map(self.hash_func, list(self.nodes)))
        self.hashring = dict(zip(hash_val, list(self.nodes)))
    
    def search_server(self, object_key: str):
        object_key_hash = self.hash_func(object_key)
        key_list = list(self.hashring) + list(map(lambda x: x + self.max_hashsize, self.hashring))
        serverindex = sorted([idx for idx in key_list if idx > object_key_hash])[0] % self.max_hashsize

        return self.hashring[serverindex]