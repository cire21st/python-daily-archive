# https://school.programmers.co.kr/learn/courses/30/lessons/131705
def solution(number):
    cnt = 0
    for i_index,i in enumerate(number):
        for j_index,j in enumerate(number[i_index+1:],start=i_index + 1):
            for k in number[j_index+1:]:
                if i+j+k == 0:
                    cnt+=1
    return cnt
