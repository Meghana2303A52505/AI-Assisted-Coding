"""Write a Python program to implement a Queue using lists.

Requirements:
- Follow FIFO principle
- Include:
  enqueue(item)
  dequeue()
  peek()
  size()

- Handle empty queue cases
- Add comments and test cases"""
class Queue:
    """A Queue implementation using lists following FIFO principle."""
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)
    
    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")
        return self.items[0]
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0


# Test cases
if __name__ == "__main__":
    q = Queue()
    
    # Test enqueue
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(f"Queue size after enqueuing 3 items: {q.size()}")  # Output: 3
    
    # Test peek
    print(f"Front item (peek): {q.peek()}")  # Output: 10
    
    # Test dequeue
    print(f"Dequeued item: {q.dequeue()}")  # Output: 10
    print(f"Queue size after dequeue: {q.size()}")  # Output: 2
    
    # Test with remaining items
    print(f"Next front item: {q.peek()}")  # Output: 20
    
    # Empty the queue
    q.dequeue()
    q.dequeue()
    print(f"Queue empty: {q.is_empty()}")  # Output: True
    
    # Test error handling
    try:
        q.dequeue()
    except IndexError as e:
        print(f"Error caught: {e}")