def solution(answers):

    # 학생별 찍은 점수
    student1 = [1, 2, 3, 4, 5] # 5개 / 5개씩 계속 반복
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8개 / 8개씩 계속 반복
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10개 / 10개씩 계속 반복

    # 점수 결과
    # return 결과 값이 1,2,3 숫자로 학생명을 표기해서 1,2,3 숫자로 Key 값으로 사용함
    # Map 구조는 {학생번호, 정답 맞춘 문제수} 형태로 저장
    # 변수 선언은 정답 맞춘 문제수가 없기에 0으로 값을 넣음
    results = {1: 0, 2: 0, 3: 0}

    # 문제 답만큼 반복하기
    for i in range(len(answers)):

        # 학생1의 찍기 답은 5개씩 반복이라, %5 연산 사용하여 답 제공
        if student1[i % 5] == answers[i]:
            # 맞추면 정답 수를 1씩 더하기
            results[1] += 1

        # 학생2의 찍기 답은 8개씩 반복이라, %8 연산 사용하여 답 제공
        if student2[i % 8] == answers[i]:
            # 맞추면 정답 수를 1씩 더하기
            results[2] += 1

        # 학생3의 찍기 답은 10개씩 반복이라, %10 연산 사용하여 답 제공
        if student3[i % 10] == answers[i]:
            # 맞추면 정답 수를 1씩 더하기
            results[3] += 1

    # 가장 높은 점수 구하기
    # results 구조의 값 중 가장 큰 숫자 가져오기
    top_score = max(results.values())

    answer = []

    # 학생이 3명이고, 학생번호는 1번부터 3번까지이기에 range(1,4) 선언함
    for i in range(1,4):
        # 가장 높은 점수를 가진 학생들만 정답자에 추가하기
        # results의 학생번호는 1,2,3 순서대로 값을 저장하기에 정렬은 필요없음
        if results[i] == top_score:
            # 학생번호 추가하기
            answer.append(i)

    return answer