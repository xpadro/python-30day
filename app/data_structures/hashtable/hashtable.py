class HashTable:
    """ Hash table implementation
    
    """


    def __init__(self, size):
        self.buckets = []
        for _ in range(size):
            self.buckets.append([])

        self.size = size
    

    def __hash_key(self, key):
        hash = 0

        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        
        return hash
    
    def set(self, key, value):
        hashed_key = self.__hash_key(key)
        bucket = self.buckets[hashed_key]

        for item in bucket:
            if item.get(key) is not None:
                item[key] = value
                return

        bucket.append({key: value})
    
    def get(self, key):
        hashed_key = self.__hash_key(key)
        bucket = self.buckets[hashed_key]

        if len(bucket) == 0:
            return None
        
        for item in bucket:
            found_item = item.get(key)
            
            if found_item:
                return found_item
        
        return None


if __name__ == "__main__":
    table = HashTable(50)

    table.set('asasxf', 10000)
    table.set('b', 'value b')
    print('get asasxf: ' + str(table.get('asasxf')))
    print('get b: ' + str(table.get('b')))
    print('get c: ' + str(table.get('c')))

    table.set('b', 33)
    print('get b: ' + str(table.get('b')))
