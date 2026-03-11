'''refactor repeated file open/read/close logic.
DRY principle
Context managers
Function reuse'''

f = open("lab 13.5/data1.txt")
print(f.read())
f.close()
f = open("lab 13.5/data2.txt")
print(f.read())
f.close()

def read_and_print_file(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found:", filename)

read_and_print_file("lab 13.5/data1.txt")
read_and_print_file("lab 13.5/data2.txt")



