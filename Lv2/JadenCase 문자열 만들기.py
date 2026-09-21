# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    #split으로 단어를 분절함
    #Upper을 [0]에 대해서만, 나머지는 lower 실행
    cnt = []
    for i in range(len(s)):
        if s[i] == ' ': cnt.append(i)
    s = s.split()
    answer = []
    for i in s:
        answer.append(i[0].upper() + i[1:].lower())
    return ' '.join(answer)
