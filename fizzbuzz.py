"""
Problem 6 and 7.

for each number from start to end. Check if the number is divisible by 3 and 5.
If it is divisible by 3 and 5, if so print fizzbuzz. Else check if it is
divisble by 3, if so print fizz else check if it is divislbe by 5, if so print
buzz. Else print number
"""


def fizzbuzz(start, end):
    for i in range(start, end+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
