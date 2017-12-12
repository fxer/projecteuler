def palindrome():
    largest = 0
    for a in range(999, 99, -1):
        for b in range(999, 99, -1):
            # use an awesome extended slice to reverse string
            # https://docs.python.org/2/whatsnew/2.3.html#extended-slices
            # print(a, b, a*b, str(a*b)[::-1])
            if a*b == int(str(a*b)[::-1]) and a*b > largest:
                largest = a*b
    return largest

print(palindrome())
