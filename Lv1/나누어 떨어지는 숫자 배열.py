# https://school.programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    result = sorted([i for i in arr if i%divisor == 0])
        
    return result if len(result) != 0 else [-1]
