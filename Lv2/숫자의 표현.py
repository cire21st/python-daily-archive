# https://school.programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    sum_i = 0 
    answer = 1 # 15 = 15
    
    # 등차수열 합공식: 1/2(l-a+1) * (a + l) = S
    for num in range(2, n//2 + 2):
        for i in range(1, n//2 + 2): # 1 ~ 8
            if i+(i+num-1) == 2*n/num: 
                answer += 1
                break

    return answer

