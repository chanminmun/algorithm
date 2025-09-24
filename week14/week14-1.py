#https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    for i in range(1,sum+1):
        if sum % i == 0:
            wid = sum //i
            if (wid - 2) * (i - 2) == yellow:
                answer = [wid,i]
                answer.sort(reverse = True)
    return answer