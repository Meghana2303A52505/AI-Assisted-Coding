#generate a code to sort student records(name,roll no,CGPA) CGPA wise in descending order for placement drive using merge sort and quick sort and compare the time taken by both sorting algorithms. compare the performance for large datasets.display top 10 students
import time

class Student:
    def __init__(self, name, roll_no, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa


def merge_sort(students):
    if len(students) > 1:

        mid = len(students) // 2
        L = students[:mid]
        R = students[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].cgpa > R[j].cgpa:
                students[k] = L[i]
                i += 1
            else:
                students[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            students[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            students[k] = R[j]
            j += 1
            k += 1


def quick_sort(students):

    if len(students) <= 1:
        return students

    pivot = students[0]

    left = [x for x in students[1:] if x.cgpa > pivot.cgpa]
    right = [x for x in students[1:] if x.cgpa <= pivot.cgpa]

    return quick_sort(left) + [pivot] + quick_sort(right)


def generate_students(n):

    students = []

    for i in range(n):

        name = f"Student{i+1}"
        roll_no = i + 1

        # Fixed CGPA pattern instead of random
        cgpa = (i % 10) + 1

        students.append(Student(name, roll_no, cgpa))

    return students


def main():

    n = 1000

    students1 = generate_students(n)
    students2 = students1.copy()

    start_time = time.time()
    merge_sort(students1)
    merge_sort_time = time.time() - start_time

    start_time = time.time()
    sorted_students_quick = quick_sort(students2)
    quick_sort_time = time.time() - start_time

    print(f"Time taken by Merge Sort: {merge_sort_time:.6f} seconds")
    print(f"Time taken by Quick Sort: {quick_sort_time:.6f} seconds")

    print("\nTop 10 students sorted by CGPA:")

    for student in sorted_students_quick[:10]:
        print(f"Name: {student.name}, Roll No: {student.roll_no}, CGPA: {student.cgpa}")


if __name__ == "__main__":
    main()