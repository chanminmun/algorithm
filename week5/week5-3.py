# https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    extend = numbers * (k*2)
    answer = 0
    for _ in range(k-1):
        answer +=2
    return extend[answer]