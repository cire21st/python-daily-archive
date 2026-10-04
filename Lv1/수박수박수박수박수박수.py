# https://school.programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = []
    for i in range(n):
        answer.append('박') if i % 2 != 0 else answer.append('수')
    return ''.join(answer)
