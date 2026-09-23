# https://school.programmers.co.kr/learn/courses/30/lessons/120880
def solution(numlist, n):
    distance = []
    result = []
    for i in numlist:
        distance.append(abs(i-n))
    #find lowest in distance and result.append()
    
    while len(distance) != 0:
        min = 20000
        min_val = 0
        for i in range(len(distance)):
            if min > distance[i] or (min == distance[i] and numlist[i] > min_val):
                min = distance[i]
                min_val = numlist[i]
                j = i
        result.append(min_val)
        distance = distance[:j] + distance[j+1:]
        numlist =  numlist[:j] + numlist[j+1:]
    
    return result
    
