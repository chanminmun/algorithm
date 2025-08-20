# https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    answer = True
    line = list(map(int,str(x)))
    hap = sum(line)
    perc = int(hap)
    if x%perc == 0:
        answer = True
    else:
        answer = False

    return answer