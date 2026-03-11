'''refactor a legacy script where multiple calculations are embedded directly inside the main code block.
Identify repeated or related logic and extract it into reusable functions.
Ensure the refactored code is modular, easy to read, and documented with docstrings.
'''
price = 250
tax = price * 0.18
total = price + tax
print("Total Price:", total)

price = 500
tax = price * 0.18
total = price + tax
print("Total Price:", total)

# Refactored Code:
def calculate_total_price(price):
    """Calculate total price including tax."""
    tax = price * 0.18
    total = price + tax
    return total
# Example usage
print("Total Price:", calculate_total_price(250))
print("Total Price:", calculate_total_price(500))
