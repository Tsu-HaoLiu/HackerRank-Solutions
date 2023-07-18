# https://www.hackerrank.com/challenges/one-month-preparation-kit-dynamic-array/problem
def dynamicArray(n, queries):
    zero_list = [[] for _ in range(n)]
    last_answer = 0
    ans = []
    
    for q in queries:
        dquery = q[0]
        
        if dquery == 1:
            x = (q[1] ^ last_answer) % n
            zero_list[x].append(q[2])
        elif dquery == 2:
            x = (q[1] ^ last_answer) % n
            last_answer = zero_list[x][q[2] % len(zero_list[x])]
            ans.append(last_answer)
    return ans
