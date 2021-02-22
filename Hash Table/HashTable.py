
class HashTable:

    def __init__(self):

        self.capacity = 10
        self.keys = [None]*self.capacity
        self.values = [None] * self.capacity

    def insert(self, key, data):

        index = self.hash_function(key)

       
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                return

       
            index = (index+1) % self.capacity

        self.keys[index] = key
        self.values[index] = data

    def get(self, key):

        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity

        return None

    def hash_function(self, key):

        hash_sum = 0

        for letter in key:
            hash_sum = hash_sum + ord(letter)

        return hash_sum % self.capacity



table = HashTable()
table.insert('Adam', 23)
table.insert('Kevin', 45)
table.insert('Peter', 34)
table.insert('John', 33)

print(table.get('John'))
print(table.hash_function("John"))

