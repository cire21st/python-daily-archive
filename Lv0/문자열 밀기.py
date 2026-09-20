# https://school.programmers.co.kr/learn/courses/30/lessons/120921
def solution(A, B):
    cnt = 0

    while A != B:
        temp = A[-1]
        A = temp + A[:-1]
        cnt += 1
        if cnt == len(A): return -1
    
    return cnt
    
