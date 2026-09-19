# https://school.programmers.co.kr/learn/courses/30/lessons/120878
def solution(a, b):
        for i in reversed(range(2,min(a,b)+1)): #a/b가 기약분수가 될때까지 나누기
            if a%i == 0 and b%i == 0:
                b = b//i
                break
        #b를 2와 5로 계속 나누었을때 1만 남는지 확인
        while(b%2 == 0 or b%5 == 0):
            b = b//2 if b%2 == 0 else b//5
        return 2 if b != 1 else 1
