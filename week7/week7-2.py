# https://school.programmers.co.kr/learn/courses/30/lessons/181890


def solution(str_list):
    answer = []
    for i in range(len(str_list)):
        if str_list[i] == "l":
            answer += str_list[:i]
            break
        if str_list[i] == "r":
            answer += str_list[i + 1:]
            break
        else:
            answer = []

    return answer