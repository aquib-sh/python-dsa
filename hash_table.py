class Node:
    def __init__(self, _key, value):
        self.key = _key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, _max=20):
        self._max_table_length = _max
        self.table = [None for i in range(self._max_table_length)]

    def hash(self, _key):
        if type(_key) == str:
            value = 0
            for char in _key:
                value += ord(char)
            _key = value
        return _key % 20
    
    def add(self, _key, value):
        address = self.hash(_key)
        if self.table[address] == None:
            self.table[self.hash(_key)] = Node(_key, value)
        else:
            head = self.table[address]
            newNode = Node(_key, value) 
            newNode.next = head
            self.table[address] = newNode

    def remove(self, _key) -> bool:
        address = self.hash(_key)
        if self.table[address] == None: return False

        current = self.table[address]
        if current.key == _key:
            self.table[address] = current.next
            return True

        while (current != None):
            prev = current 
            current = current.next
            if current.key == _key:
                prev.next = current.next
                return True
        return False

    def get(self, _key):
        address = self.hash(_key)
        if self.table[address] != None:
            current = self.table[address]
            while (current != None):
                if current.key == _key:
                    return current.value
                current = current.next
        return None

    def __str__(self):
        _str = "[\n"
        for i in range(0, self._max_table_length):
            _str += f"{i} ->"
            
            if self.table[i] == None: 
                _str += "\n"
                continue

            current = self.table[i]
            while current != None:
                _str += f"[{current.key}:{current.value}] ->"
                current = current.next
            _str += "\n"
        _str += "\n]"

        return _str


if __name__ == "__main__":
    hashmap = HashTable()
    hashmap.add(20, 40)
    hashmap.add(30, 400)
    hashmap.add(90, 690)
    hashmap.add(110, 388)

    hashmap.add(545, 60)
    hashmap.add(457, 90)
    hashmap.add(44, 100)

    hashmap.add("name", "Aquib")
    hashmap.add("age", 23)
    hashmap.add("city", "Mumbai")
    hashmap.add("degree", "M.Sc Computer Science")

    print(hashmap)
    
    hashmap.remove(44)
    hashmap.remove(90)
    hashmap.remove(43)
    hashmap.remove("degree")

    print(hashmap)
