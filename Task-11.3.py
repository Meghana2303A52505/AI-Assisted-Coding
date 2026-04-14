"""Task 1: Smart Contact Manager (Arrays & Linked Lists)
Scenario
SR University’s student club requires a simple Contact Manager Application to store members’ names and phone numbers. The system should support efficient addition, searching, and deletion of contacts.
Tasks
1.	Implement the contact manager using arrays (lists).
2.	Implement the same functionality using a linked list for dynamic memory allocation.
3.	Implement the following operations in both approaches:
o	Add a contact
o	Search for a contact
o	Delete a contact
4.	Use GitHub Copilot to assist in generating search and delete methods.
5.	Compare array vs. linked list approaches with respect to:
o	Insertion efficiency
o	Deletion efficiency
Expected Outcome
•	Two working implementations (array-based and linked-list-based).
•	A brief comparison explaining performance differences.
"""


# class ContactManagerArray:
#     def __init__(self):
#         self.contacts = []
#     def add_contact(self, name, phone):
#         self.contacts.append({"name": name, "phone": phone})
#         print("Contact added")
#     def search_contact(self, name):
#         for contact in self.contacts:
#             if contact["name"] == name:
#                 print("Found:", contact["name"], "-", contact["phone"])
#                 return
#         print("Contact not found")
#     def delete_contact(self, name):
#         for contact in self.contacts:
#             if contact["name"] == name:
#                 self.contacts.remove(contact)
#                 print("Contact deleted")
#                 return
#         print("Contact not found")
#     def display_contacts(self):
#         print("\nArray Contacts:")
#         for contact in self.contacts:
#             print(contact["name"], "-", contact["phone"])
# class Node:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#         self.next = None
# class ContactManagerLinkedList:
#     def __init__(self):
#         self.head = None
#     def add_contact(self, name, phone):
#         new_node = Node(name, phone)
#         if self.head is None:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = new_node
#         print("Contact added")
#     def search_contact(self, name):
#         temp = self.head
#         while temp:
#             if temp.name == name:
#                 print("Found:", temp.name, "-", temp.phone)
#                 return
#             temp = temp.next
#         print("Contact not found")
#     def delete_contact(self, name):
#         temp = self.head
#         prev = None
#         while temp:
#             if temp.name == name:
#                 if prev is None:
#                     self.head = temp.next
#                 else:
#                     prev.next = temp.next
#                 print("Contact deleted")
#                 return
#             prev = temp
#             temp = temp.next
#         print("Contact not found")
#     def display_contacts(self):
#         print("\nLinked List Contacts:")
#         temp = self.head
#         while temp:
#             print(temp.name, "-", temp.phone)
#             temp = temp.next
# print("ARRAY IMPLEMENTATION")
# array_manager = ContactManagerArray()
# array_manager.add_contact("Rahul", "9876543210")
# array_manager.add_contact("Anita", "9123456780")
# array_manager.display_contacts()
# array_manager.search_contact("Rahul")
# array_manager.delete_contact("Rahul")
# array_manager.display_contacts()
# print("\nLINKED LIST IMPLEMENTATION")
# linked_manager = ContactManagerLinkedList()
# linked_manager.add_contact("Rahul", "9876543210")
# linked_manager.add_contact("Anita", "9123456780")
# linked_manager.display_contacts()
# linked_manager.search_contact("Anita")
# linked_manager.delete_contact("Rahul")
# linked_manager.display_contacts()

"""Task 2: Library Book Search System (Queues & Priority Queues)
Scenario
The SRU Library manages book borrow requests. Students and faculty submit requests, but faculty requests must be prioritized over student requests.
Tasks
1.	Implement a Queue (FIFO) to manage book requests.
2.	Extend the system to a Priority Queue, prioritizing faculty requests.
3.	Use GitHub Copilot to assist in generating:
o	enqueue() method
o	dequeue() method
4.	Test the system with a mix of student and faculty requests.
Expected Outcome
•	Working queue and priority queue implementations.
•	Correct prioritization of faculty requests.
"""


# from collections import deque
# class LibraryQueue:
#     def __init__(self):
#         self.queue = deque()
#     def enqueue(self, name, book, role):
#         request = (name, book, role)
#         self.queue.append(request)
#         print("Request added:", request)
#     def dequeue(self):
#         if not self.queue:
#             print("No requests in queue")
#             return
#         request = self.queue.popleft()
#         print("Processing request:", request)
#     def display(self):
#         print("\nQueue Requests:")
#         for req in self.queue:
#             print(req)
# import heapq
# class LibraryPriorityQueue:
#     def __init__(self):
#         self.pq = []
#     def enqueue(self, name, book, role):
#         # Faculty gets higher priority
#         if role.lower() == "faculty":
#             priority = 1
#         else:
#             priority = 2
#         heapq.heappush(self.pq, (priority, name, book, role))
#         print("Request added:", name, book, role)
#     def dequeue(self):
#         if not self.pq:
#             print("No requests")
#             return
#         request = heapq.heappop(self.pq)
#         print("Processing:", request[1], "-", request[2], "-", request[3])
#     def display(self):
#         print("\nPriority Queue Requests:")
#         for req in sorted(self.pq):
#             print(req[1], "-", req[2], "-", req[3])
# print("NORMAL QUEUE SYSTEM")
# q = LibraryQueue()
# q.enqueue("Rahul", "Data Structures", "Student")
# q.enqueue("Anita", "Machine Learning", "Faculty")
# q.enqueue("Kiran", "Python Programming", "Student")
# q.display()
# q.dequeue()
# q.dequeue()
# q.display()
# print("\nPRIORITY QUEUE SYSTEM")
# pq = LibraryPriorityQueue()
# pq.enqueue("Rahul", "Data Structures", "Student")
# pq.enqueue("Anita", "Machine Learning", "Faculty")
# pq.enqueue("Kiran", "Python Programming", "Student")
# pq.enqueue("Dr. Rao", "Artificial Intelligence", "Faculty")
# pq.display()
# pq.dequeue()
# pq.dequeue()
# pq.display()


"""Task 3: Emergency Help Desk (Stack Implementation)
Scenario
SR University’s IT Help Desk receives technical support tickets from students and staff. While tickets are received sequentially, issue escalation follows a Last-In, First-Out (LIFO) approach.
Tasks
1.	Implement a Stack to manage support tickets.
2.	Provide the following operations:
o	push(ticket)
o	pop()
o	peek()
3.	Simulate at least five tickets being raised and resolved.
4.	Use GitHub Copilot to suggest additional stack operations such as:
o	Checking whether the stack is empty
o	Checking whether the stack is full (if applicable)
Expected Outcome
•	Functional stack-based ticket management system.
•	Clear demonstration of LIFO behavior.
"""

# class HelpDeskStack:
#     def __init__(self, size):
#         self.stack = []
#         self.size = size
#     # Check if stack is empty
#     def is_empty(self):
#         return len(self.stack) == 0
#     # Check if stack is full
#     def is_full(self):
#         return len(self.stack) == self.size
#     # Push operation
#     def push(self, ticket):
#         if self.is_full():
#             print("Stack is full. Cannot add ticket.")
#         else:
#             self.stack.append(ticket)
#             print("Ticket added:", ticket)
#     # Pop operation
#     def pop(self):
#         if self.is_empty():
#             print("No tickets to resolve.")
#         else:
#             ticket = self.stack.pop()
#             print("Resolved ticket:", ticket)
#     # Peek operation
#     def peek(self):
#         if self.is_empty():
#             print("No tickets available.")
#         else:
#             print("Latest ticket:", self.stack[-1])
#     # Display stack
#     def display(self):
#         print("\nCurrent Tickets in Stack:")
#         for ticket in reversed(self.stack):
#             print(ticket)
# helpdesk = HelpDeskStack(10)
# # Raising tickets
# helpdesk.push("Ticket 1: WiFi not working")
# helpdesk.push("Ticket 2: Printer issue")
# helpdesk.push("Ticket 3: Login problem")
# helpdesk.push("Ticket 4: Software installation")
# helpdesk.push("Ticket 5: Email not syncing")
# helpdesk.display()
# # Peek latest ticket
# helpdesk.peek()
# # Resolving tickets (LIFO)
# helpdesk.pop()
# helpdesk.pop()
# helpdesk.display()

"""Task 4: Hash Table
Objective
To implement a Hash Table and understand collision handling.
Task Description
Use AI to generate a hash table with:
•	Insert
•	Search
•	Delete
Starter Code
class HashTable:
pass
Expected Outcome
•	Collision handling using chaining
•	Well-commented methods
"""

# class HashTable:
#     def __init__(self, size):
#         # Create hash table with empty buckets
#         self.size = size
#         self.table = [[] for _ in range(size)]
#     # Hash function
#     def hash_function(self, key):
#         return key % self.size
#     # Insert method
#     def insert(self, key, value):
#         index = self.hash_function(key)
#         # Check if key already exists
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         # Add new key-value pair
#         self.table[index].append([key, value])
#         print("Inserted:", key, value)
#     # Search method
#     def search(self, key):
#         index = self.hash_function(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 print("Found:", pair)
#                 return pair[1]
#         print("Key not found")
#         return None
#     # Delete method
#     def delete(self, key):
#         index = self.hash_function(key)
#         for i, pair in enumerate(self.table[index]):
#             if pair[0] == key:
#                 self.table[index].pop(i)
#                 print("Deleted key:", key)
#                 return
#         print("Key not found")
#     # Display hash table
#     def display(self):
#         print("\nHash Table:")
#         for i, bucket in enumerate(self.table):
#             print(i, ":", bucket)
# ht = HashTable(5)
# ht.insert(10, "Python")
# ht.insert(15, "Java")
# ht.insert(20, "C++")
# ht.insert(7, "JavaScript")
# ht.display()
# ht.search(15)
# ht.delete(20)
# ht.display()

"""Task 5: Real-Time Application Challenge
Scenario
Design a Campus Resource Management System with the following features:
•	Student Attendance Tracking
•	Event Registration System
•	Library Book Borrowing
•	Bus Scheduling System
•	Cafeteria Order Queue
Student Tasks
1.	Choose the most appropriate data structure for each feature.
2.	Justify your choice in 2–3 sentences.
3.	Implement one selected feature using AI-assisted code generation.
Expected Outcome
•	Mapping table: Feature → Data Structure → Justification
•	One fully working Python implementation
"""

# from collections import deque
# class CafeteriaQueue:
#     def __init__(self):
#         self.orders = deque()
#     # Place new order
#     def place_order(self, order):
#         self.orders.append(order)
#         print("Order placed:", order)
#     # Serve order
#     def serve_order(self):
#         if not self.orders:
#             print("No orders to serve")
#         else:
#             order = self.orders.popleft()
#             print("Serving order:", order)
#     # Display all orders
#     def display_orders(self):
#         print("\nCurrent Orders in Queue:")
#         for order in self.orders:
#             print(order)
# cafeteria = CafeteriaQueue()
# cafeteria.place_order("Burger")
# cafeteria.place_order("Pizza")
# cafeteria.place_order("Sandwich")
# cafeteria.place_order("Coffee")
# cafeteria.place_order("Pasta")
# cafeteria.display_orders()
# cafeteria.serve_order()
# cafeteria.serve_order()
# cafeteria.display_orders()

