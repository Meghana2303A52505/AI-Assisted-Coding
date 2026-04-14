#generate a code to implement bubble sort with ai comments and provide time complexity analysis
import time
class Student:
    def __init__(self, name, roll_no, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa

def bubble_sort(students):
    n = len(students)

    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if students[j].cgpa < students[j+1].cgpa:
                students[j], students[j+1] = students[j+1], students[j]
def generate_students(n):
    students = []

    for i in range(n):
        name = f"Student_{i+1}"
        roll_no = i + 1
        cgpa = round(5.0 * (i + 1) / n, 2)  # Generate CGPA between 0 and 5
        students.append(Student(name, roll_no, cgpa))

    return students
if __name__ == "__main__":
    n = 10  # Number of students to generate
    students = generate_students(n)

    print("Before sorting:")
    for student in students:
        print(f"{student.name}: {student.cgpa}")

    start_time = time.time()
    bubble_sort(students)
    end_time = time.time()

    print("\nAfter sorting:")
    for student in students:
        print(f"{student.name}: {student.cgpa}")

    print(f"\nTime taken to sort: {end_time - start_time:.6f} seconds")
# Time Complexity Analysis:
# The time complexity of bubble sort is O(n^2) in the worst and average cases
# because it requires two nested loops to compare each element with every other element.
# In the best case, when the list is already sorted, the time complexity is O(n)
# because it only requires one pass to check if the list is sorted. However, bubble sort is generally not efficient for large datasets compared to other sorting algorithms like merge sort or quick sort.
