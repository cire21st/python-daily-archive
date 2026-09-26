# https://school.programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    return sum((map(lambda a,b: a*b, sorted(A), sorted(B, reverse = True))))
