# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    max_w = 0
    max_h = 0
    for w, h in sizes:
        wid = max(w, h)
        hei = min(w, h)
        max_w = max(max_w, wid)
        max_h = max(max_h, hei)

    return max_w * max_h

    return answer