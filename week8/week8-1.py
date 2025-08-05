# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    for i in range(1 ,len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1

    for n in range(1 ,len(food)):
        for j in range(food[n ]//2):
            answer += str(n)

    answer = answer + "0" + answer[::-1]


    return answer