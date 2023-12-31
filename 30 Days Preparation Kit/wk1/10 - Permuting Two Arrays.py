# https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem

def twoArrays(k, A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return 'NO'
    return 'YES'
