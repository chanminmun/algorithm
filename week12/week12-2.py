# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter


def solution(k, tangerine):
    counts = Counter(tangerine)
    sorted_counts = sorted(counts.values(), reverse=True)

    answer = 0
    total_tangerines = 0

    for count in sorted_counts:
        answer += 1
        total_tangerines += count

        if total_tangerines >= k:
            break

    return answer