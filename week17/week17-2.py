#https://school.programmers.co.kr/learn/courses/30/lessons/142085
def solution(n, k, enemy):
    import heapq
    answer = 0
    heap = []
    i = 0

    while i < len(enemy):
        e = enemy[i]
        heapq.heappush(heap, e)
        if len(heap) > k:
            n -= heapq.heappop(heap)
        if n < 0:
            break
        answer += 1
        i += 1

    return answer