from typing import List, Dict, Any
import bisect

# AI Recommendation:
# For searching by appointment ID, Binary Search is suitable if the data is sorted by ID; otherwise, Linear Search.
# For sorting, use Python's built-in sort (Timsort), which is efficient for both time and consultation fee.

# Justification:
# - Binary Search: O(log n) time, fast for sorted lists.
# - Linear Search: O(n) time, simple for unsorted lists.
# - Timsort: O(n log n) time, stable and efficient for real-world data.


class AppointmentManager:
    def __init__(self, appointments: List[Dict[str, Any]]):
        self.appointments = appointments

    def linear_search_by_id(self, appointment_id: str) -> Dict[str, Any]:
        for appt in self.appointments:
            if appt['appointment_id'] == appointment_id:
                return appt
        return None

    def binary_search_by_id(self, appointment_id: str) -> Dict[str, Any]:
        # Assumes appointments are sorted by appointment_id
        ids = [appt['appointment_id'] for appt in self.appointments]
        idx = bisect.bisect_left(ids, appointment_id)
        if idx < len(ids) and ids[idx] == appointment_id:
            return self.appointments[idx]
        return None

    def sort_by_time(self):
        self.appointments.sort(key=lambda x: x['appointment_time'])

    def sort_by_fee(self):
        self.appointments.sort(key=lambda x: x['consultation_fee'])

# Example usage:
if __name__ == "__main__":
    appointments = [
        {'appointment_id': 'A101', 'patient_name': 'John', 'doctor_name': 'Dr. Smith', 'appointment_time': '2024-06-12 10:00', 'consultation_fee': 500},
        {'appointment_id': 'A102', 'patient_name': 'Alice', 'doctor_name': 'Dr. Jones', 'appointment_time': '2024-06-12 09:00', 'consultation_fee': 300},
        {'appointment_id': 'A103', 'patient_name': 'Bob', 'doctor_name': 'Dr. Lee', 'appointment_time': '2024-06-12 11:00', 'consultation_fee': 400},
    ]

    manager = AppointmentManager(appointments)

    # Linear search (unsorted)
    print("Linear Search:", manager.linear_search_by_id('A102'))

    # Sort by appointment_id for binary search
    manager.appointments.sort(key=lambda x: x['appointment_id'])
    print("Binary Search:", manager.binary_search_by_id('A103'))

    # Sort by time
    manager.sort_by_time()
    print("Sorted by Time:", manager.appointments)

    # Sort by fee
    manager.sort_by_fee()
    print("Sorted by Fee:", manager.appointments)