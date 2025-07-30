# https://school.programmers.co.kr/learn/courses/30/lessons/12977


from itertools import combinations


def solution(nums):
    answer = 0
    result = []

    for comb in combinations(nums, 3):
        total = sum(comb)
        result.append(total)

    for value in result:

        if value < 2:
            continue

        prime = True

        for j in range(2, int(value ** 0.5) + 1):
            if value % j == 0:
                prime = False
                break
        if prime:
            answer += 1
    return answer
