#https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    lists = s.split(' ')
    for i in range(len(lists)):
        listss = lists[i]
        if listss:
            lists[i] = listss[0].upper() + listss[1:].lower()
    return ' '.join(lists)