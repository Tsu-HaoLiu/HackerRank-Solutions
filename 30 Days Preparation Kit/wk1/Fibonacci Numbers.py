# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    if n <= 1:
        return n

    prev = 0
    curr = 1
    
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr