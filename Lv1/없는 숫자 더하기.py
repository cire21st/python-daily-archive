# https://school.programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    cnt = 0
    for i in range(1,10):
        if i not in numbers: cnt+=i
        
    return cnt
