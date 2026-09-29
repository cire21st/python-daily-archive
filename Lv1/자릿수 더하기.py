# https://school.programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    sum = 0
    for i in reversed(range(0,len(str(n)))):
        sum += n // 10**i
        n = n % 10**i

    return sum
