# https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/problem

def caesarCipher(s, k):
    default = 'abcdefghijklmnopqrstuvwxyz'
    shift = default[k%26:] + default[:k%26]
    hashmap = {str(k): str(v) for k, v in zip(default, shift)}
    
    ans = ''
    for i in s:
        if i.isupper():
            ans += hashmap[i.lower()].upper()
            continue
        
        if i.isalpha():
            ans += hashmap[i]
            continue
        
        ans += i
        
    return ans

# ----

def caesarCipher(s, k):
    ans = ''
    
    for i in s:
        if i.isalpha():
            char_code = ord(i)
            if 65 <= char_code <= 90:
                current_letter = (char_code - 65 + k) % 26 + 65
                print(current_letter)
            elif 97 <= char_code <= 122:
                current_letter = (char_code - 97 + k) % 26 + 97

            ans += chr(current_letter) 
            continue
        
        ans += i
    return ans
