#https://school.programmers.co.kr/learn/courses/30/lessons/181860?language=python3

def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i] == True:
            answer += [arr[i]] * (arr[i]*2)
        else:
            answer = answer[:-arr[i]]
    return answer
