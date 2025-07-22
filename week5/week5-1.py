# https://school.programmers.co.kr/learn/courses/30/lessons/181921

def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        check = True
        for s in str(i):
            if s != "5" and s != "0":
                check = False
                break
        if check == True:
            answer.append(i)

    if answer == []:
        answer = [-1]
    return answer