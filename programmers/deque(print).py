from collections import deque

def solution(priorities, location):
    answer = 0

    # deque 구조만들기
    # 키 : [2, 1, 3, 2] 값으로 설정 / 값 : location과 매칭할 인덱스
    # myDeque 변수 값 : deque([(2, 0), (1, 1), (3, 2), (2, 3)])
    myDeque = deque([(v,i) for i,v in enumerate(priorities)])

    # print(myDeque)

    while myDeque:

        # 첫번째 값 가져오고, myDeque에서 삭제하기
        firstData = myDeque.popleft()

        # myDeque 데이터가 존재하고, 우선 가장 높은 데이터가 가져온 데이터보다 크다면,
        if myDeque and max(myDeque)[0] > firstData[0]:

            # 가져온 데이터를 뒤에 추가하기
            # myDeque 변수 값 : deque([(3, 2), (2, 3), (2, 0), (1, 1)])
            myDeque.append(firstData)
            # print(myDeque)

        else: # 우선순위 가장 높은 것을 찾은 상태에서 location에 해당되는 값 찾기
            # 우선수위 높은 것 찾으면,
            # 더이상 가져오고, 추가하기 안함
            # 멈춘 상태 : deque([(2, 3), (2, 0), (1, 1)])

            # 대기열 값 구하기
            answer += 1

            # 문서 찾으면, 더이상 반복하지 않기
            if location == firstData[1]:
                break
    return answer