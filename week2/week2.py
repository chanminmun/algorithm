def solution(a, b):
    answer = 0
    sm = int(str(a) + str(b))
    time = 2 * a * b

    if sm > time:
        answer = sm
    else:
        answer = time
    return answer


a = int(input("a:"))
b = int(input("b:"))

print(solution(a, b))