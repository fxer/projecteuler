# starting Fibonacci numbers
fib = [0, 1]
total = 0
while sum(fib) <= 4000000:
    # sum the even numbers
    if sum(fib) % 2 == 0:
        total += sum(fib)

    nextfib = sum(fib)
    fib[0] = fib[1]
    fib[1] = nextfib

print(total)
