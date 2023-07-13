# https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem

def matchingStrings(strings, queries):
    ans = []
    
    for q in queries:
        ans.append(strings.count(q))
        
    return ans
