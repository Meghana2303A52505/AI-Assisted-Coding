import heapq
from enum import Enum


"""Choose appropriate data structures and justify:

1. Traffic Signal Queue
2. Emergency Vehicle Priority
3. Vehicle Registration Lookup
4. Road Network Mapping
5. Parking Slot Tracking

Output as table with justification
Write a Python program for Emergency Vehicle Priority using Priority Queue.

Requirements:
- Ambulances highest priority
- Include:
  add_vehicle(type, priority)
  process_vehicle()

- Use heapq"""

class VehicleType(Enum):
    AMBULANCE = 1
    FIRE_TRUCK = 2
    POLICE = 3
    REGULAR = 4

class EmergencyVehicleQueue:
    def __init__(self):
        self.queue = []
        self.vehicle_count = 0
    
    def add_vehicle(self, vehicle_type, priority=None):
        if priority is None:
            priority = vehicle_type.value
        self.vehicle_count += 1
        heapq.heappush(self.queue, (priority, self.vehicle_count, vehicle_type.name))
    
    def process_vehicle(self):
        if not self.queue:
            return None
        priority, count, vehicle_type = heapq.heappop(self.queue)
        return f"Processing {vehicle_type} (Priority: {priority})"

# Data structures justification
data_structures = [
    ["Traffic Signal Queue", "Queue (FIFO)", "Vehicles arrive in order, first come first served"],
    ["Emergency Vehicle Priority", "Priority Queue (Min Heap)", "Process ambulances/fire trucks before regular traffic"],
    ["Vehicle Registration Lookup", "Dictionary/Hash Map", "O(1) lookup by registration number"],
    ["Road Network Mapping", "Graph (Adjacency List)", "Represent intersections and roads efficiently"],
    ["Parking Slot Tracking", "Set/Hash Set", "Quick check for available slots, O(1) operations"]
]

print("\n--- Emergency Vehicle Priority System ---\n")

queue = EmergencyVehicleQueue()
queue.add_vehicle(VehicleType.AMBULANCE, 1)
queue.add_vehicle(VehicleType.REGULAR, 4)
queue.add_vehicle(VehicleType.FIRE_TRUCK, 2)
queue.add_vehicle(VehicleType.POLICE, 3)

while queue.queue:
    print(queue.process_vehicle())
