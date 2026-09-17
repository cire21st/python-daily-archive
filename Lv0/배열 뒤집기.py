# https://school.programmers.co.kr/learn/courses/30/lessons/120821
def solution(num_list):
    return_list = []
    for i in range(1,len(num_list)+1):
        return_list.append(num_list[-i])
    return return_list
