'''refactor a given Python script that contains multiple repeated code blocks.
Prompt AI to identify duplicate logic and replace it with functions or classes.
Ensure the refactored code maintains the same output.
Add docstrings to all functions.'''

print("Area of Rectangle:", 5 * 10)
print("Perimeter of Rectangle:", 2 * (5 + 10))

print("Area of Rectangle:", 7 * 12)
print("Perimeter of Rectangle:", 2 * (7 + 12))

print("Area of Rectangle:", 10 * 15)
print("Perimeter of Rectangle:", 2 * (10 + 15))
# Refactored Code:
def calculate_rectangle_properties(length, width):
    """Calculate and print the area and perimeter of a rectangle."""
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area of Rectangle: {area}")
    print(f"Perimeter of Rectangle: {perimeter}")
# Example usage
calculate_rectangle_properties(5, 10)
calculate_rectangle_properties(7, 12)
calculate_rectangle_properties(10, 15)
