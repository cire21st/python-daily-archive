# https://school.programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = n
    for i in range(1,n//2+1):
        answer += i if n%i == 0 else 0
    return answer
