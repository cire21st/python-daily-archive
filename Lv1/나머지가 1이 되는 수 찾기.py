# https://school.programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    i = 1
    while n % i != 1:
        i += 1
    return i
