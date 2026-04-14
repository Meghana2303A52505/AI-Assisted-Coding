"""Write a Python program to implement a Singly Linked List.

Requirements:
- Create Node class (data, next)
- Create LinkedList class

Methods:
  insert(data)
  display()

- Add docstrings and comments
- Demonstrate with sample data"""
class Node:
    """A node in the singly linked list."""
    def __init__(self, data):
        """Initialize a node with data and next pointer."""
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list implementation."""
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def insert(self, data):
        """Insert a new node with data at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        """Print all elements in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")


# Demonstrate with sample data
if __name__ == "__main__":
    ll = LinkedList()
    
    # Insert sample data
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    ll.insert(20)
    
    # Display the linked list
    print("Linked List:")
    ll.display()