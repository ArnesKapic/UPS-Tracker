# Part A: Developing a hash table
# Part B: Develop a lookup function
# HashTable implementation using chaining with lists
class HashTable:
    # Initializing the hash table with a given capacity
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]  # Creating empty buckets

    # Adding a new key-value pair or update an existing key
    def add(self, key, value):
        index = self._hash_function(key)  # Computing hash index
        bucket = self.table[index]  # Selecting appropriate bucket

        # Checking if key already exists and update its value if found
        for i in range(len(bucket)):
            if bucket[i][0] == key:  # Key exists, update value
                bucket[i][1] = value
                return True

        # If key is not found, append a new [key, value] pair
        bucket.append([key, value])
        return True

    # Searching for the value associated with a given key
    def lookup(self, key):
        index = self._hash_function(key)  # Computing hash index
        bucket = self.table[index]  # Selecting appropriate bucket

        # Looking for the key in the bucket and return the corresponding value
        for k, v in bucket:
            if k == key:
                return v  # Returning value if key is found

        # Returning None if key is not present in the hash table
        return None

    # Hash function to compute index for a given key
    def _hash_function(self, key):
        return hash(key) % self.capacity  # Ensuring index fits within the table size
