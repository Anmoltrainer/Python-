# Raising an Exception: You can raise an exception explicitly using the raise statement. For example:

x = 10
if x > 5:
    raise ValueError("x should be less than or equal to 5")


# Catching an Exception: You can catch and handle exceptions using try, except, and optionally, else and finally blocks. For example:

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)


# Creating and Raising User-Defined Exceptions:

class MyCustomError(Exception):
    pass

def my_function(x):
    if x < 0:
        raise MyCustomError("Negative values are not allowed")
    return x * 2


# Use of Assertions in Python:

x = 10
assert x > 0, "x should be greater than 0"


