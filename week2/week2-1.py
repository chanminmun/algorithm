def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])
    answer = max
    return answer
#정렬 후 가장 작은수의 곱과 가장큰 수의 곱 비교 후 max 값 도출
#정수 배열 numbers가 매개변수로 주어집니다.
#numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.