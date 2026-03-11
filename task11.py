'''Refactor the given poorly structured Python script into a clean, modular, and reusable implementation.'''
# Harshad Number Checker (Unstructured Version)

num = int(input("Enter a number: "))

temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    temp = temp // 10

if sum_digits != 0:
    if num % sum_digits == 0:
        print("True")
    else:
        print("False")
else:
    print("False")
# Refactored Code:
def is_harshad_number(num):
    """Check if a number is a Harshad number."""
    if num < 0:
        return "Input must be a non-negative integer."
    
    sum_digits = sum(int(digit) for digit in str(num))
    
    if sum_digits == 0:
        return False
    
    return num % sum_digits == 0
# Example usage
num = int(input("Enter a number: "))
result = is_harshad_number(num)
print(result)