# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    comp = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        if i in comp:
            comp.remove(i)
    answer=sum(comp)
    return answer