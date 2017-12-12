import math
import sys

# don't actually need to check if the divisor is prime, it will just happen
# that way according to the https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
def isprime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, math.floor(math.sqrt(n))+1):
            if n % x == 0:
                return False
    return True

def factor(n):
    # start searching the first prime, 2, as the divisor
    i = 2
    # only need to check divisors up to sqrt(n), this is a nice description why
    # https://math.stackexchange.com/a/1039525
    while i <= math.sqrt(n):
        # if we find an even divisor, that is a prime factor!
        # reduce n by this divisor and continue searching for larger prime factors
        if n % i == 0:
            # print(i, n // i)
            n = n // i
        i += 1
    return n

# recursive version loosely based on
# https://stackoverflow.com/a/33609588/1107232
def factor_recursion(n):
    if n <= 3:
        return n
    elif n % 2 == 0:
        return factor_recursion(n//2)
    elif n % 3 == 0:
        return factor_recursion(n//3)
    else:
        for i in range(5, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                return factor_recursion(n//i)

    return n

print(factor(int(sys.argv[1])))
print(factor_recursion(int(sys.argv[1])))
