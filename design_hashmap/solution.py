'''
Solution to the design hashmap problem
'''
class MyHashMap:
    '''
    Main class : Solution to the design hashmap problem
    '''
    def __init__(self):
        '''
        Init function
        '''
        # Save the hashmap as a dict
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        '''
        Add item to hashmap dict
        '''
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        '''
        Return -1 if hash key not available, 
        Return value if hash key available
        '''
        return self.hash_map.get(key, -1)

    def remove(self, key: int) -> None:
        '''
        Try to remove the key
        '''
        try:
            self.hash_map.pop(key)
        except Exception as e:
            print(e)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)