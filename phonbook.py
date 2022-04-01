# 풀이 방법
#
# 문자열 기반 정렬을 통해 비슷한 문자끼리 순서를 변경함
# 문자의 길이가 아닌 문자열 내용으로 정렬
#
# 정렬 전 : ["119", "97674223", "1195524421"]
# 정렬 후 : ['119', '1195524421', '97674223']
#
# 정렬 후, 현재 기준 값이 다음 값에 포함되는지 체크함
def solution(phone_book):

    # 문자열 값에 따라 정렬
    phone_book.sort()

    # 출력 결과
    answer = True

    # 반복 횟수
    phone_length = len(phone_book)

    # 기준이 되는 번호이며, 마지막까지 반복할 필요가 없어 마지막 전까지 반복
    for i in range(phone_length-1):

        # 기준되는 번호와 다음 번호 값의 앞의 번호(기준되는 번호 길이만큼) 같은지 비교
        # 예 : 기준번호 : 119(3글자) / 다음 번호 97674223 중 3번째 문자인 976까지
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:

            answer = False # 맞으면 false로 변경

            # 맞았으니, 더 이상 반복문 그만 실행하기
            break

        return answer