# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
