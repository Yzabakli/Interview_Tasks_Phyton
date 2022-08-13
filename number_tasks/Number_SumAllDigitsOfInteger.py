def digSum(n):
    if n < 10:
        return n

    temp = 0

    while n > 0:
        temp += int(n) % 10

        n /= 10

    return int(temp)


n = 1234
print(digSum(n))
