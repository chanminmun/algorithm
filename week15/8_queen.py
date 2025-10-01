pos = [0] * 8
flag = [False] * 8       # 열 사용 여부
flag_a = [False] * 15    # ↘ 대각선 사용 여부 (row + col)
flag_b = [False] * 15    # ↙ 대각선 사용 여부 (row - col + 7)

def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end=" ")
    print()

def set(i: int) -> None:
    for j in range(8):
        if not flag[j] and not flag_a[i + j] and not flag_b[i - j + 7]:
            pos[i] = j
            if i == 7:
                put()
            else:
                flag[j] = flag_a[i + j] = flag_b[i - j + 7] = True
                set(i + 1)
                flag[j] = flag_a[i + j] = flag_b[i - j + 7] = False

set(0)
