def isArmstrong(number):
    number_to_string = str(number)

    power = len(number_to_string)

    temp = 0

    i = 0

    while i < len(number_to_string):
        temp += pow(int(number_to_string[i:i + 1]), power)

        i += 1

    return temp == number


print(isArmstrong(155047533421450153908889))
