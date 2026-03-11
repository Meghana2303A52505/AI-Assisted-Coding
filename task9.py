'''Twin primes are pairs of primes that differ by 2 (e.g., 11 and 13, 17 and 19).'''
# twin primes bad version
a=11
b=13
fa=0
for i in range(2,a):
 if a%i==0:
  fa=1
fb=0
for i in range(2,b):
 if b%i==0:
  fb=1
if fa==0 and fb==0 and abs(a-b)==2:
 print("Twin Primes")
else:
 print("Not Twin Primes")
# Refactored Code:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def are_twin_primes(a, b):
    if abs(a - b) == 2 and is_prime(a) and is_prime(b):
        return "Twin Primes"
    else:
        return "Not Twin Primes"
# Example usage
print(are_twin_primes(11, 13))
