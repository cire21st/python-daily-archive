# https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    sum_x = 0
    for c in str(x):
        sum_x += int(c)
    
    return True if x % sum_x == 0 else False
