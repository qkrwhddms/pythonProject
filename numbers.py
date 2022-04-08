def solution(numbers):

    #초기 데이터 타입 알아보자
    print(type(numbers)) #List 구조
    print(type(numbers[0])) #List<int> 구조

    # List안의 값을 String타입으로 변경하기
    # List<int> => List<String>
    # str => 문자열(String타입)로 변경해주는 함수
    # list => list 구조 만들어주는 함수
    numbers = list(map(str, numbers))

    # 변경된 데이터 타입 조회하기
    print(type(numbers)) #List 구조
    print(type(numbers[0])) #List<String> 구조

    # 람다를 이용하여 정렬 numbers 변수에 들어가는 숫자는 최대 1000까지이므로,
    # 정렬을 위한 반복횟수는 최대 3자리수로 맞춤
    # 내림차순을 위헤 reverse=True
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))