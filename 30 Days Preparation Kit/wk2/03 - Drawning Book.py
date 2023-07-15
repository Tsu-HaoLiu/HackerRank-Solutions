# https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/problem

def pageCount(n, p):
    if n % 2 == 0:
        n += 1
    
    return min(p // 2, (n - p) // 2)
    
    # if n % 2 == 0:
    #     n = n + 1
    # start = p//2
    # end = (n-p)//2
    # return min(start,end)
