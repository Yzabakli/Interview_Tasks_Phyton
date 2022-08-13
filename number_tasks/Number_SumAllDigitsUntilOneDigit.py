def sumAllDigitsUntilOneDigit(n):
    while n > 9:

        digit = n
        s = 0

        while digit > 0:
            s += int(digit) % 10

            digit = digit / 10

        print(s)

        n = s


sumAllDigitsUntilOneDigit(797897)
