from collections import deque

# 데큐 데이터 생성하기
myDeque = deque([(1, "첫번째"), (2, "두번째"), (3, "세번째"), (4, "네번째"), (5, "다섯번째")])

# 출력
print("전체 데큐 : ", myDeque)

# 왼쪽 내용 가져오기, 가져오면 삭제됨
firstData = myDeque.popleft()

# 삭제한 데이터
print("왼쪽 첫번째 데이터 : ", firstData)

print("현재 데큐 : ", myDeque)

# 방금 가져온 첫번째 데이터를 추가하기
myDeque.append(firstData)
print("현재 데큐 : ", myDeque)