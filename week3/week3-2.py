# https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i%2 == 0:
            answer+=i
    return answer
