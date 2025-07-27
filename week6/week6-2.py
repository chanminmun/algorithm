#https://school.programmers.co.kr/learn/courses/30/lessons/77484
def rank(x):
    if x >= 2:
        return 7 - x
    else:
        return 6


def solution(lottos, win_nums):
    includezero = 0
    nozero = 0
    for num in lottos:
        if num in win_nums:
            includezero += 1
            nozero += 1
        elif num == 0:
            includezero += 1

    mxrank = rank(includezero)
    mirank = rank(nozero)

    answer = [mxrank, mirank]

    return answer