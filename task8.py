from collections import deque
from datetime import datetime

"""Suggest data structures and justify:

1. Shopping Cart
2. Order Processing
3. Top-Selling Products
4. Product Search
5. Delivery Routes

Output in table format
Write a Python program for Order Processing using Queue.

Requirements:
- FIFO order processing
- Include:
  place_order(order)
  process_order()

- Add comments and test cases"""
# Data Structures Recommendation Table
data_structures = [
    ["Shopping Cart", "List/Dictionary", "Fast add/remove items, easy to modify quantities"],
    ["Order Processing", "Queue (FIFO)", "Ensures orders processed in sequence, fair processing"],
    ["Top-Selling Products", "Heap/Priority Queue", "Quick access to top products by sales count"],
    ["Product Search", "Hash Table/Dictionary", "O(1) lookup time for product by ID or name"],
    ["Delivery Routes", "Graph", "Efficiently represent connections between locations"]
]



# Order Processing using Queue
class OrderQueue:
    """FIFO Order Processing System using Queue"""
    
    def __init__(self):
        self.queue = deque()
        self.order_counter = 0
    
    def place_order(self, order):
        """Add order to queue"""
        self.order_counter += 1
        order_details = {
            'order_id': self.order_counter,
            'items': order,
            'timestamp': datetime.now(),
            'status': 'Pending'
        }
        self.queue.append(order_details)
        print(f"✓ Order #{order_details['order_id']} placed: {order}")
    
    def process_order(self):
        """Process order from front of queue (FIFO)"""
        if not self.queue:
            print("No orders to process!")
            return None
        
        order = self.queue.popleft()
        order['status'] = 'Processed'
        print(f"✓ Order #{order['order_id']} processed: {order['items']}")
        return order
    
    def view_queue(self):
        """Display all pending orders"""
        if not self.queue:
            print("Queue is empty")
        else:
            print(f"Pending orders: {len(self.queue)}")
            for order in self.queue:
                print(f"  - Order #{order['order_id']}: {order['items']}")


# Test Cases
print("TEST CASES - Order Processing System\n")

# Test 1: Basic order placement and processing
print("Test 1: FIFO Order Processing")
processor = OrderQueue()
processor.place_order("Laptop, Mouse")
processor.place_order("Keyboard, Monitor")
processor.place_order("USB Cable, Adapter")
processor.view_queue()
print()

processor.process_order()
processor.process_order()
print()

# Test 2: Process empty queue
print("Test 2: Process from Empty Queue")
processor.process_order()
processor.process_order()
print()

# Test 3: Mixed operations
print("Test 3: Mixed Operations")
processor.place_order("Headphones")
processor.place_order("Speaker")
processor.view_queue()
processor.process_order()
processor.view_queue()