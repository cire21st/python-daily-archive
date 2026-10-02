# https://school.programmers.co.kr/learn/courses/30/lessons/12973#
def solution(s):
    remaining = []
    
    for ch in s:
        if remaining and ch == remaining[-1]: remaining.pop()
        else: remaining.append(ch)
        
    return 1 if remaining==[] else 0
