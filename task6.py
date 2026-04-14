import heapq

"""For the following hospital system features, choose the best data structure and justify in 2–3 sentences:

1. Patient Check-In System
2. Emergency Case Handling
3. Medical Records Storage
4. Doctor Appointment Scheduling
5. Hospital Room Navigation

Use:
Stack, Queue, Priority Queue, Linked List, BST, Graph, Hash Table, Deque

Write a Python program to implement Emergency Case Handling using a Priority Queue.

Requirements:
- Higher severity → higher priority
- Include:
  add_patient(name, severity)
  treat_patient()

- Use heapq
- Add comments and test cases"""
# Data Structure Choices & Justifications:
# 1. Patient Check-In System → Queue: FIFO order ensures fair processing
# 2. Emergency Case Handling → Priority Queue: Severity-based prioritization for critical patients
# 3. Medical Records Storage → Hash Table: O(1) lookup by patient ID for fast retrieval
# 4. Doctor Appointment Scheduling → BST: Sorted by time enables efficient range queries
# 5. Hospital Room Navigation → Graph: Models hospital layout with rooms as nodes and paths as edges

class EmergencyCaseHandler:
    """Priority Queue implementation for hospital emergency cases"""
    
    def __init__(self):
        self.patients = []  # Min-heap (negate severity for max-heap)
        self.patient_count = 0
    
    def add_patient(self, name, severity):
        """Add patient with severity (1-10, 10=critical)"""
        # Negate severity for max-heap behavior in Python's min-heap
        heapq.heappush(self.patients, (-severity, self.patient_count, name))
        self.patient_count += 1
        print(f"Patient {name} added with severity {severity}")
    
    def treat_patient(self):
        """Remove and treat highest priority patient"""
        if not self.patients:
            print("No patients waiting")
            return None
        
        neg_severity, _, name = heapq.heappop(self.patients)
        severity = -neg_severity
        print(f"Treating {name} (severity: {severity})")
        return name

# Test Cases
if __name__ == "__main__":
    handler = EmergencyCaseHandler()
    
    handler.add_patient("John", 3)
    handler.add_patient("Alice", 9)
    handler.add_patient("Bob", 5)
    handler.add_patient("Carol", 10)
    
    print("\nTreating patients in priority order:")
    handler.treat_patient()  # Carol (10)
    handler.treat_patient()  # Alice (9)
    handler.treat_patient()  # Bob (5)
    handler.treat_patient()  # John (3)
    handler.treat_patient()  # Empty