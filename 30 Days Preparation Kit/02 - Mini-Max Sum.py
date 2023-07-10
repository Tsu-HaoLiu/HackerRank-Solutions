# https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem

def miniMaxSum(arr):
    arr.sort()
    
    mini = sum(arr[:4])
    maxi = sum(arr[1:])
    
    print(f'{mini} {maxi}')