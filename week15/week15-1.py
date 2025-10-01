#https://school.programmers.co.kr/learn/courses/30/lessons/12911

def same(x: int, y: int) -> bool:
    return bin(x).count('1') == bin(y).count('1')


def solution(n):
    answer = 0
    bigger = n
    while True:
        bigger += 1
        if same(n, bigger) == True:
            answer += bigger
            break

    return answer