# Task 2: Loops and comprehensions

# Q1: Print odd numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# Q2: Use list comprehension to create a list of squares.
numbers = [1, 2, 3, 4, 5]
squares = [i ** 2 for i in numbers]
print(squares)

# Q3: Use dictionary comprehension to map each number to its cube.
number_cubes = {i: i ** 3 for i in range(1, 6)}
print(number_cubes)
