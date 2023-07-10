# https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem

def plusMinus(arr):
    total = len(arr)
    hashmap = {'pos': 0, 'neg': 0, 'neut': 0}
    
    for i in arr:
        # negative
        if i < 0:
            hashmap['neg'] += 1/total
        
        # zero
        if i == 0:
            hashmap['neut'] += 1/total
        
        # positive
        if i > 0:
            hashmap['pos'] += 1/total
    
    for i in hashmap.values():
        print(i)
        
    