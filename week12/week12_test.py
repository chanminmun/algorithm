from typing import Any


class FixedQueue:  # 고정 길이 원형 큐 클래스

    class Empty(Exception):  # 큐가 비었을 때 예외
        pass

    class Full(Exception):  # 큐가 가득 찼을 때 예외
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.no = 0  # 현재 데이터 개수
        self.front = 0  # 맨 앞 인덱스
        self.rear = 0  # 맨 뒤 인덱스
        self.capacity = capacity  # 큐의 최대 크기 (← 원래 코드에서 0으로 되어 있던 부분 수정)
        self.que = [None] * capacity  # 큐 본체 (배열)

    def __len__(self) -> int:
        return self.no  # len(queue) 호출 시 크기 반환

    def is_empty(self) -> bool:
        return self.no <= 0  # 비어있으면 True

    def is_full(self) -> bool:
        return self.no >= self.capacity  # 꽉 차면 True

    def enque(self, x: Any) -> None:  # 데이터 삽입
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:  # 끝까지 갔으면 처음으로
            self.rear = 0

    def deque(self) -> Any:  # 데이터 꺼내기
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:  # 끝까지 갔으면 처음으로
            self.front = 0
        return x

    def peek(self) -> Any:  # 맨 앞 데이터 확인
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:  # 원하는 값 찾기
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx  # 찾으면 인덱스 반환
        return -1  # 없으면 -1

    def count(self, value: Any) -> int:  # 특정 값 개수 세기
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:  # in 연산자 지원
        return self.count(value) > 0

    def clear(self) -> None:  # 큐 비우기
        self.no = self.front = self.rear = 0

    def dump(self) -> None:  # 전체 데이터 출력
        if self.is_empty():
            print("queue is empty")
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()
