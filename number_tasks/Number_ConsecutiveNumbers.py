import string


def consecutive_numbers(number):
    for n in range(number):

        if n != 0:

            if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:

                print("CodilityTestCoders")

            elif n % 2 == 0 and n % 3 == 0:

                print("CodilityTest")

            elif n % 2 == 0 and n % 5 == 0:

                print("CodilityCoders")

            elif n % 5 == 0 and n % 3 == 0:

                print("TestCoders")

            elif n % 2 == 0:

                print("Codility")

            elif n % 3 == 0:

                print("Coders")

            elif n % 5 == 0:

                print("Test")

            else:

                print(n)


consecutive_numbers(24)
