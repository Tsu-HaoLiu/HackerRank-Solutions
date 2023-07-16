# https://www.hackerrank.com/challenges/one-month-preparation-kit-angry-children/problem

def maxMin(k, arr):
    arr.sort()
    ans = float('inf')
    
    for i in range(len(arr)-k + 1):
        min_fair = arr[i]
        max_fair = arr[i+k-1]
        ans = min(ans, max_fair-min_fair)
    
    return ans
