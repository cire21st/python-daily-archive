# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    #t에서 len(p) 만큼의 수들을 전부 찾기
    #찾은 수를 p와 비교해서 p보다 작거나 같으면 cnt +=1
    cnt = 0
    for i in range(len(t)-len(p) + 1):
        if t[i:len(p)+ i] <= p: cnt+=1
        
    return cnt
