'''Refactor code that modifies shared mutable state.
Functional-style refactoring
Predictability'''

data = []
def add_item(x):
    data.append(x)
add_item(10)
add_item(20)
print(data)
# Refactored Code:
def add_item(data, x):
    return data + [x]
# Example usage
data = []
data = add_item(data, 10)
data = add_item(data, 20)
print(data)
