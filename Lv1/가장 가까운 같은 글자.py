# https://school.programmers.co.kr/learn/courses/30/lessons/142086?language=python3
def solution(s):
    answer = [-1]
    for i in range(len(s)):
        for j in reversed(range(i)):
            if s[i] == s[j]: 
                answer.append(i-j);
                break;
            if j==0: answer.append(-1);
            
    return answer
