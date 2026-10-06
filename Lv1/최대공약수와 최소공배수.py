# https://school.programmers.co.kr/learn/courses/30/lessons/12940
def solution(n, m):
    answer = []
    common_div = 0
    common_mul = 0
    for i in range(1,min(n,m) + 1):
        if n % i == 0 and m % i == 0 : common_div = i
    j = max(n,m)
    while(common_mul != j):
        if j % n == 0 and j % m == 0 : common_mul = j
        else: j += 1
        
        
    return common_div,common_mul
