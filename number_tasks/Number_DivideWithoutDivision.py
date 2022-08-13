def divide(dividend, divisor):
    result = 0

    while dividend >= divisor:
        dividend -= divisor
        result += 1

    return {"Quotient": result, "Remainder": dividend}


print(divide(75, 4))
