# https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    cnt = 0
    if s[0] == '(' and s[-1] == ')':
        for i in s:
            if cnt == 0 and i == ')': return False
            cnt+= 1 if i == '(' else -1
        if cnt == 0: return True
    return False
