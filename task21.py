'''refactor a performance-heavy loop handling large data.
Algorithmic optimization
Use of built-in functions'''

total = 0
for i in range(1, 1000000):
    if i % 2 == 0:
        total += i
print(total)
# Refactored Code:
total = sum(i for i in range(1, 1000000) if i % 2 == 0)
print(total)
