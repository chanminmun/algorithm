#문제 설명
#당신은 어떤 행사의 입장 조건을 프로그래밍하고 있습니다. 다음 조건을 만족하지 않는 사람은 입장할 수 없습니다.
#나이는 18세 이상이어야 하며,
#티켓을 소지하고 있어야 합니다.

#사용자로부터 나이(age)와 티켓 소지 여부(has_ticket: True 또는 False)를 입력받아,
#입장 가능 여부를 출력하세요.

age = int(input("나이를 입력하세요"))
ticket = input("티켓이 있나요?(True/False):")
ticket = True if ticket == "True" else False
if age < 18 or not ticket:
    print("입장불가")
else:
    print("입장가능")