# https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/problem

def pangrams(s):
    # 97 - 122
    return 'pangram' if len(set(s.replace(' ', '').lower())) == 26 else 'not pangram'