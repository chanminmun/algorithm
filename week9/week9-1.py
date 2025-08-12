# https://school.programmers.co.kr/learn/courses/30/lessons/181188
def solution(targets):
    answer = 0
    target_sort = sorted(targets, key=lambda interval: interval[1])

    current = 0

    cnt = 0

    for s, e in target_sort:
        if s < current < e:
            continue

        current = e - 0.5

        cnt += 1

    return cnt