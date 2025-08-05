#https://school.programmers.co.kr/learn/courses/30/lessons/120868

def solution(sides):
    answer = 0
    max = sides[0] + sides[1]
    bigside = 0
    shortside = 0
    if sides[0] > sides[1]:
        bigside = sides[0]
        shortside = sides[1]
    else:
        bigside = sides[1]
        shortside = sides[0]

    for i in range(max):
        if shortside + i > bigside and max > bigside:
            answer += 1

    return answer