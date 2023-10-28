# Here's the basic syntax of a list comprehension:

# new_list = [expression for item in iterable if condition]

# For example, here's a list comprehension that squares each number in a list and only includes the squared values that are even:

numbers = [1, 2, 3, 4, 5]
squared_evens = [x**2 for x in numbers if x % 2 == 0]


# Example using map() with a lambda function to square a list of numbers:

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))


# Example using map() to convert a list of strings to uppercase:

words = ["hello", "world"]
uppercase_words = list(map(str.upper, words))


# Example using reduce() to find the product of all elements in a list:

from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)


# Example using filter() to filter out even numbers from a list:

numbers = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
