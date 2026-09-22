# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    #문자열을 순회함
    #공백은 공백, 공백이후 문자는 대문자, 문자or숫자이후 문자는 소문자
    result = []
    for i in range(len(s)):
        if s[i] == ' ': result.append(' ')
        elif i == 0 or s[i-1] == ' ': result.append(s[i].upper())
        else :result.append(s[i].lower())

    return ''.join(result)
