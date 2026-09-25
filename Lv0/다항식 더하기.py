# https://school.programmers.co.kr/learn/courses/30/lessons/120863#
def solution(polynomial):
    polynomial = polynomial.split(" + ")
    x_coefficient = 0
    bias = 0
    
    for i in polynomial:
        if i == 'x': x_coefficient += 1
        elif i != 'x' and i.endswith('x'): x_coefficient += int(i[:-1])
        else: bias += int(i)
    
    if x_coefficient == 0: answer_x = ''
    elif x_coefficient == 1: answer_x = 'x'
    else: answer_x = str(x_coefficient) + 'x'
    
    if bias == 0 : answer_y = ''
    elif bias != 0 and x_coefficient == 0: answer_y = str(bias)
    else: answer_y = " + " + str(bias)
    
    return answer_x + answer_y
