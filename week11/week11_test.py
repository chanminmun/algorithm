from typing import Any   # 타입 힌트를 위해 Any 가져옴

class FixedStack:   # 고정 길이 스택 클래스

    class Empty(Exception):  # 스택이 비었을 때 발생하는 예외
        pass

    class Full(Exception):   # 스택이 가득 찼을 때 발생하는 예외
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity   # 스택을 저장할 리스트 (고정 크기)
        self.capacity = capacity       # 스택 용량
        self.ptr = 0                   # 스택 포인터 (현재 원소 개수)

    def __len__(self) -> int:
        return self.ptr   # 스택에 들어 있는 데이터 수 반환

    def is_empty(self) -> bool:
        return self.ptr <= 0   # 스택이 비었는지 확인

    def is_full(self) -> bool:
        return self.ptr >= self.capacity   # 스택이 가득 찼는지 확인



    def push(self, value: Any) -> None:
        if self.is_full():            # 가득 찼으면 예외 발생
            raise FixedStack.Full
        self.stk[self.ptr] = value    # 값 추가
        self.ptr += 1                 # 포인터 이동

    def pop(self) -> Any:
        if self.is_empty():  # 스택이 비었는지 확인
            raise FixedStack.Empty
        self.ptr -= 1  # 포인터 줄여서 삭제 효과
        return self.stk[self.ptr]  # 줄인 위치가 바로 맨 위 원소

    def peek(self) -> Any:
        if self.is_empty():  # 스택이 비었는지 확인
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]  # 맨 위 원소 반환 (포인터 유지)

    def clear(self) -> None:
        self.ptr = 0   # 스택 비우기 (리스트 초기화 대신 포인터만 리셋)



    def find(self, value: Any) -> Any:
        # 스택에서 value를 뒤쪽부터 탐색 → 발견 시 인덱스 반환
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1  # 없으면 -1 반환

    def count(self, value: Any) -> int:
        # 스택에 있는 value 개수 세기
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        # in 연산자 지원 (value in stack)
        return self.count(value) > 0

    def dump(self) -> None:
        # 스택 내용 출력
        if self.is_empty():
            print("stack is empty")
        else:
            print(self.stk[:self.ptr])   # 실제 데이터만 출력
