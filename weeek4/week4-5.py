#문제 4: 좌표 격자 출력
#문제 설명
#정수 N이 주어졌을 때, N x N 형태의 좌표를 아래와 같이 출력하세요.

n = int(input())

for i in range(0,n):
    for j in range(0,n):
        print(f"({i},{j})", end ="")
    print()