def divExp(a, b):
    assert a > 0, "Value of 'a' must be greater than 0"

    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    c = a / b
    return c


try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    result = divExp(a, b)
    print("Result =", result)

except AssertionError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)