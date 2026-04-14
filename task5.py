from datetime import datetime
from typing import List, Dict, Optional

# Data structure for allocation details
class Allocation:
    def __init__(self, student_id: str, room_number: int, floor: int, allocation_date: str):
        self.student_id = student_id
        self.room_number = room_number
        self.floor = floor
        self.allocation_date = datetime.strptime(allocation_date, "%Y-%m-%d")

    def __repr__(self):
        return (f"Allocation(student_id={self.student_id}, room_number={self.room_number}, "
                f"floor={self.floor}, allocation_date={self.allocation_date.date()})")

# Optimized search: Use a dictionary for O(1) lookup by student_id
class HostelManagementSystem:
    def __init__(self):
        self.allocations: List[Allocation] = []
        self.student_index: Dict[str, Allocation] = {}

    def add_allocation(self, allocation: Allocation):
        self.allocations.append(allocation)
        self.student_index[allocation.student_id] = allocation

    def search_by_student_id(self, student_id: str) -> Optional[Allocation]:
        return self.student_index.get(student_id)

    # Optimized sort: Use Python's built-in Timsort (sorted()), which is stable and efficient
    def sort_by_room_number(self) -> List[Allocation]:
        return sorted(self.allocations, key=lambda x: x.room_number)

    def sort_by_allocation_date(self) -> List[Allocation]:
        return sorted(self.allocations, key=lambda x: x.allocation_date)

# Justification:
# - Dictionary indexing allows O(1) search for student_id.
# - Python's sorted() uses Timsort, which is O(n log n) and stable, ideal for sorting records.

# Example usage
if __name__ == "__main__":
    hms = HostelManagementSystem()
    hms.add_allocation(Allocation("S001", 101, 1, "2024-06-01"))
    hms.add_allocation(Allocation("S002", 102, 1, "2024-06-03"))
    hms.add_allocation(Allocation("S003", 201, 2, "2024-06-02"))

    print("Search by student ID S002:", hms.search_by_student_id("S002"))
    print("Sorted by room number:", hms.sort_by_room_number())
    print("Sorted by allocation date:", hms.sort_by_allocation_date())