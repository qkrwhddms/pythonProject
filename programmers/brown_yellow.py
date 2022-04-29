def solution(brown, yellow):
    answer = []

    # ab = Yellow + Brown 수식확인
    # Brown = 10 / Yellow = 2
    # ab = 12
    ab = brown + yellow

    # 전체 네모칸 만큼 반복하기
    for b in range(1, ab+1):

        # a 길이를 구하기 위해 ab를 b로 나눠 떨어지는 것만 계산하기
        if (ab / b) % 1 == 0:

            # ab = 12
            # a = 12 / b => a 0 ab / b
            a = ab / b

            # 전체 조건으로 a는 무조건 b보다 크던지 같기 때문에 조건 추가
            if a >= b:

                # 갈색 구하기 : Brown = 2a + 2a -4
                # 2a + 2b = Brown + 4
                if 2*a + 2*b == brown + 4: # 2*a + 2*b = brown + 4
                    return [a,b]