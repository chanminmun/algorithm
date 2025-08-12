# https://school.programmers.co.kr/learn/courses/30/lessons/64065


def solution(s):
    s = s.lstrip('{').rstrip('}')
    parts = s.split("},{")

    sets = []
    for p in parts:
        numb = list(map(int, p.split(',')))
        sets.append(numb)

    sets.sort(key=len)

    answer = []
    for se in sets:
        for numb in se:
            if numb not in answer:
                answer.append(numb)
    return answer