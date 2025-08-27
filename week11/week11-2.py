# https://school.programmers.co.kr/learn/courses/30/lessons/131127
def solution(want, number, discount):
    answer = 0
    want_dict = {w: n for w, n in zip(want, number)}

    for i in range(len(discount) - 9):
        window = discount[i:i+10]
        check = {}
        for item in window:
            if item in want_dict:
                if item not in check:
                    check[item] = 1
                else:
                    check[item] += 1
        ok = True
        for w in want_dict:
            if check.get(w, 0) < want_dict[w]:
                ok = False
                break

        if ok:
            answer += 1

    return answer