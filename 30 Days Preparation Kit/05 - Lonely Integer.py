# https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem

def lonelyinteger(a):
    for num in a:
        if a.count(num) == 1:
            return num