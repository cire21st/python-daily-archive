# https://school.programmers.co.kr/learn/courses/30/lessons/12930?language=python3
def solution(s):
    words = s.split(" ");
    new_words = []
    
    for word in words:
        mod_word = [c.upper() if i%2==0 else c.lower() for i,c in enumerate(word)]            
        new_words.append(''.join(mod_word))

    return ' '.join(new_words)
