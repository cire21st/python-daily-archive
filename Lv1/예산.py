# https://school.programmers.co.kr/learn/courses/30/lessons/12982?language=python3
def solution(d, budget):
    d.sort()
    cnt = 0
    while(1):
        if len(d) != 0 and d[0] <= budget:
            budget -=d[0]
            d.pop(0)
            cnt +=1
        else: return cnt 
