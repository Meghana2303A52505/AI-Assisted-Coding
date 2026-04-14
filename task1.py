"""Write a Python program to implement a Stack.

Requirements:
- Use list-based implementation
- Include methods:
  push(item)
  pop()
  peek()
  is_empty()

- Add docstrings for each method
- Handle edge cases (empty stack)
- Include example usage"""
class Stack:
    """A list-based implementation of a Stack data structure."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack.
        
        Args:
            item: The element to add to the stack.
        """
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack.
        
        Returns:
            The top item of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it.
        
        Returns:
            The top item of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty.
        
        Returns:
            True if stack is empty, False otherwise.
        """
        return len(self.items) == 0


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    print("Pushing elements: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    print(f"Peek: {stack.peek()}")  # Output: 30
    print(f"Is empty: {stack.is_empty()}")  # Output: False
    
    print(f"Popping: {stack.pop()}")  # Output: 30
    print(f"Popping: {stack.pop()}")  # Output: 20
    
    print(f"Peek: {stack.peek()}")  # Output: 10
    print(f"Popping: {stack.pop()}")  # Output: 10
    print(f"Is empty: {stack.is_empty()}")  # Output: True
    
    # Handle edge case
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error: {e}")
