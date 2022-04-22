'''
Solution to the design hashmap problem
'''
class MyHashMap:

    def __init__(self):
        print("Starting class")
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        print(key, self.hash_map.get(key, -1))
        return self.hash_map.get(key, -1)

    def remove(self, key: int) -> None:
        try:
            self.hash_map.pop(key)
        except Exception as e:
            print(e)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)