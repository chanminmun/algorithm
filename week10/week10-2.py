# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = 0
    a = []
    for i in range(2,n):
        if n%i == 1:
            a.append(i)
    a.sort()
    answer = int(a[0])
    return answer