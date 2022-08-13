def reverseInteger(num):
    temp = 0

    while int(num) != 0:
        temp = (temp * 10) + (int(num % 10))
        num /= 10

    return int(temp)


print(reverseInteger(473573657))
