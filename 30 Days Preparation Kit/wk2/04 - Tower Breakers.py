# https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/problem

def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    
    return 1
