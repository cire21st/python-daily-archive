# https://school.programmers.co.kr/learn/courses/30/lessons/120816
def solution(slice, n):
    pizza = 0
    while(n > (pizza * slice)):
        if n > (pizza * slice): pizza += 1 
        else: break 
    return pizza
