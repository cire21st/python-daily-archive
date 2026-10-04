# https://school.programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    cnt = 0
    while(cnt != 500):
        if num == 1: return cnt 
        elif num % 2 == 0: num = num/2
        else: num = num * 3 + 1
        cnt +=1
    return cnt if cnt != 500 else -1
