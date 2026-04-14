"""Write a Python program to implement a Hash Table using chaining.

Requirements:
- Use list of lists
- Include:
  insert(key, value)
  search(key)
  delete(key)

- Handle collisions using chaining
- Add comments and test cases"""
class HashTable:
    """Hash table implementation using chaining to handle collisions."""
    
    def __init__(self, size=10):
        """Initialize hash table with given size."""
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Generate hash value for a given key."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # Check if key already exists and update it
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Add new key-value pair to the chain
        self.table[index].append((key, value))
    
    def search(self, key):
        """Search for a key and return its value, or None if not found."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False
    
    def display(self):
        """Display the hash table."""
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")


# Test cases
if __name__ == "__main__":
    ht = HashTable(5)
    
    # Test insert
    print("--- Testing Insert ---")
    ht.insert("name", "Alice")
    ht.insert("age", 25)
    ht.insert("city", "NYC")
    ht.insert("country", "USA")
    ht.insert("job", "Engineer")
    ht.display()
    
    # Test search
    print("\n--- Testing Search ---")
    print(f"Search 'name': {ht.search('name')}")
    print(f"Search 'age': {ht.search('age')}")
    print(f"Search 'unknown': {ht.search('unknown')}")
    
    # Test delete
    print("\n--- Testing Delete ---")
    ht.delete("age")
    print(f"After deleting 'age': {ht.search('age')}")
    ht.display()
    
    # Test update
    print("\n--- Testing Update ---")
    ht.insert("name", "Bob")
    print(f"Updated 'name': {ht.search('name')}")