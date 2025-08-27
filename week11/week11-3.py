# https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort(reverse = True)
    h = 0
    for i in range(len(citations)):
        if citations[i] >= i+1:
            h += 1
        else:
            break
    return h