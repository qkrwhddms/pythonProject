import math

# 순서대로 정렬되어 있음을 가정
su = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]

# 최대값
max_su = max(su)
print("max_su : ", max_su)

# 소수를 구한 숫자만큼 반복
for i in su:

    # 비고 숫자의 제곱근과 최대값이 작은 경우에만 소수 찾기 진행
    if math.sqrt(i) < max_su:

        # 배수 삭제를 위해 전체 반복
        for j in su:

            # 자기 자신을 제외하고, 배수인 항목 제거
            if j > i and j % i == 0:
                print("i : ", i, " / j : ", j)

                # 삭제하기
                su.remove(j)