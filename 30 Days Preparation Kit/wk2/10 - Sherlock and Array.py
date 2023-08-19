# https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-array/problem

def balancedSums(arr):
    # arr = [5, 6, 8, 11]

    total_arr = sum(arr) # 30
    left = 0
    for each in arr: # 6
        if total_arr - each - left == left:
            return 'YES'
        else:
            left += each
        
    return 'NO'
