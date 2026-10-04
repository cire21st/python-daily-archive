# https://school.programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    arr.remove((sorted(arr,reverse=True)).pop())
    return [-1] if len(arr) == 0 else arr
