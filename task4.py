'''refactor procedural input–processing logic into functions.
Identify input, processing, and output sections.
Convert each into a separate function.
Improve code readability without changing behavior.
'''
num = int(input("Enter number: "))
square = num * num
print("Square:", square)
# Refactored Code:
def get_input():
    return int(input("Enter number: "))
def process_input(num):
    return num * num
def output_result(square):
    print("Square:", square)
# Example usage
number = get_input()
result = process_input(number)
output_result(result)
