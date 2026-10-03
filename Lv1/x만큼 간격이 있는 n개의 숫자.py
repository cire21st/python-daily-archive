# https://school.programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []
    i = 1
    while(len(answer) != n):
        answer.append(x*i)
        i += 1
    return answer
