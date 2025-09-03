# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        found = False

        for j in range(i + 1, len(numbers)):

            if numbers[j] > numbers[i]:
                answer.append(numbers[j])
                found = True
                break

        if not found:
            answer.append(-1)

    return answer


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i, num in enumerate(numbers):
        while stack and num > numbers[stack[-1]]:
            idx = stack.pop()
            answer[idx] = num
        stack.append(i)

    return answer