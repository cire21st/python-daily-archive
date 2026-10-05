# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = []
    for i in range(left,right + 1):
        cnt = 0
        for j in range(1,i+1):
            if i % j == 0: cnt+= 1
        answer.append(i)if cnt % 2 == 0 else answer.append(-i)
            
    return sum(answer)
