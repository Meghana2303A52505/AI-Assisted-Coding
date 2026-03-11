''': Generate Lucas sequence up to n terms.(Starts with 2,1, then Fn = Fn-1 + Fn-2)
Normal: 5 → [2, 1, 3, 4, 7]
Edge: 1 → [2]
Negative: -5 → Error
Large: 10 (last element = 76).
'''
def lucas_sequence(n):
    """Generate Lucas sequence up to n terms."""
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    sequence = []
    a, b = 2, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
# Example usage
print(lucas_sequence(5))
print(lucas_sequence(1))
try:
    print(lucas_sequence(-5))
except ValueError as e:
    print(e)
print(lucas_sequence(10))
