# https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem

def flippingBits(n):
    return ~n & 0xFFFFFFFF
