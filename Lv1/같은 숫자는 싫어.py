# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if len(answer) == 0 or answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer
