# https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/problem

def countingSort(arr):
    arr_len = len(arr)
    answer = [0] * arr_len if arr_len <= 100 else [0] * 100
    # print(len(answer), len(arr))
    
    for i in arr:
        answer[i] += 1
    
    return answer
