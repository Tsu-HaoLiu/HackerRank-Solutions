# https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem

def birthday(s, d, m):

    start = 0
    end = m
    count = 0
    
    while end <= len(s): 
        segment = s[start:end]
        
        if sum(segment) == d and len(segment) == m:
            count += 1
        
        start += 1
        end += 1
    
    return count
