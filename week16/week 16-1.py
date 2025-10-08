#https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    stk = []  # 보조
    current = 1  # 다음 상자
    idx = 0  # 지금 상자
    n = len(order)

    while current <= n:
        if order[idx] == current:
            idx += 1
            current += 1


        elif stk and stk[-1] == order[idx]:
            stk.pop()
            idx += 1

        else:
            stk.append(current)
            current += 1

        while stk and idx < n and stk[-1] == order[idx]:
            stk.pop()
            idx += 1

    return idx