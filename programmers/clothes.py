def solution(clothes):

    # headgear, eyewear, face 등 옷 종류별로 구분하기
    clothesTypeMap = {}

    for clothe, clothesType, in clothes:
        print(clothe)
        print("clothesType : ", clothesType)

        # 옷 종류마다 값을 1씩 더하기
        clothesTypeMap[clothesType] = clothesTypeMap.get(clothesType, 0) + 1

        print(clothesTypeMap)

    # 옷을 입지 않은 계산하기
    answer = 1
    for clothesType in clothesTypeMap:
        answer *= (clothesTypeMap[clothesType] + 1)

    # 아무것도 옷을 입지 않은 경우 빼기
    return answer -1