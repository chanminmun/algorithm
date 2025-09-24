# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for idx, ans in enumerate(answers):
        if ans == first[idx % len(first)]:
            scores[0] += 1
        if ans == second[idx % len(second)]:
            scores[1] += 1
        if ans == third[idx % len(third)]:
            scores[2] += 1

    max_score = max(scores)

    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i + 1)

    return answer