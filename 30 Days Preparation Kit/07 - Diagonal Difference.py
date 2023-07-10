# https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem

def diagonalDifference(arr):
    left = 0
    right = 0
    
    rows = len(arr)
    cols = len(arr[0]) - 1
    
    for row in range(rows):
        left += arr[row][row]
        right += arr[row][cols-row]
    
    return abs(left-right)
