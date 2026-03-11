'''Refactor the given poorly structured Python script into a clean, modular, and efficient implementation.
The program calculates the number of trailing zeros in n! (factorial of n).
Problem Statement
Calculates the full factorial (inefficient for large n)
Mixes input handling with business logic
Uses print statements instead of return values
Lacks modular structure and documentation
You must refactor the code to improve efficiency, readability, and maintainability.
'''
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
count = 0
while fact % 10 == 0:
    count = count + 1
    fact = fact // 10
print("Trailing zeros:", count)
# Refactored Code:
def count_trailing_zeros(n):
    """Calculate the number of trailing zeros in n! (factorial of n)."""
    if n < 0:
        return ("Input must be a non-negative integer.")
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
    return count
# Example usage
n = int(input("Enter a number: "))
print("Trailing zeros:", count_trailing_zeros(n))
