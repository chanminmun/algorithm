# 만든문제

import random
def solution():
    collect = random.randrange(1,101)
    while True:
        n = int(input("정답:"))
        if collect == n:
            print("정답입니다!")
            break
        elif collect>n:
            print("정답보다 작아요")
        else:
            print("정답보다 커요")
print("숫자맞추기 게임 범위는 1부터 100까지")
solution()
