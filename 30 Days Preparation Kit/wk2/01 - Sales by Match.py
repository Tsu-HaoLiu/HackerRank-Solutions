# https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem

def sockMerchant(n, ar):

    # item = ar.pop()
    # pair = 0
    
    # while len(ar) > 0:
    #     if item in ar:
    #         ar.remove(item)
    #         pair += 1
        
    #     if len(ar) > 0:
    #         item = ar.pop()
        
    # return pair
    
    pair = 0
    socks = {}
    
    for color in ar:
        if color in socks:
            pair += 1
            socks.pop(color)
        else:
            socks[color] = 1
    
    return pair
    