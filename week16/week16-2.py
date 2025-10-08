#https://school.programmers.co.kr/learn/courses/30/lessons/12980
'''def solution(n):
    ans = 0
    distance = 0
    while True:
        if distance == n:
            break
        elif distance == 0:
            distance += 1
            ans += 1
        elif distance > 0:
            distance = distance * 2
        elif distance == n-1:
            distance +=1
            ans +=1


    return ans'''

'''def solution(n):
    ans = 0
    while n>0:
        if n % 2 == 0:
            n //= 2
        else:
            n-=1
            ans += 1
    return ans'''


def solution(n: int) -> int:
    ans = 0
    while n:
        n &= n - 1  # 최하위 1비트 제거
        ans += 1  # 제거된 1비트 갯수 누적 = 점프 횟수
    return ans