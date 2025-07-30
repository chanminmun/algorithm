#https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    answer = 0
    measure = []
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                count += 1
                if j != i // j:
                    count += 1

        measure.append(count)
    for n in range(len(measure)):
        if measure[n] <= limit:
            answer += measure[n]
        else:
            answer += power

    return answer