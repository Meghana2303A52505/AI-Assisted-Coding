'''Generate Collatz sequence until reaching 1.
Normal: 6 → [6,3,10,5,16,8,4,2,1]
Edge: 1 → [1]
Negative: -5
Large: 27 (well-known long sequence)'''
def collatz_sequence(n):
    """Generate Collatz sequence until reaching 1."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence
# Example usage
print(collatz_sequence(6))
print(collatz_sequence(1))
try:
    print(collatz_sequence(-5))
except ValueError as e:
    print(e)

