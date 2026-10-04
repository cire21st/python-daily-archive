# https://school.programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    return sum([abs if sign else abs * -1 for abs,sign in zip(absolutes,signs)])
