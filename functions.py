# Solution to problem 10
def factorial_recursive(num):
    if num > 1:
        print(num * factorial_recursive(num - 1))
    else:
        print("\n")
