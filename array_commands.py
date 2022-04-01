def solution(array, commands):
    answer = []

    # command 명령 수 세기
    cmd_length = len(commands)

    # command 명령만큼 반복하기
    for i in range(cmd_length):

        # 첫번째 배열값과 두번째 배열값에 해당되는 범위를 commands에서 가져오기
        # 인덱스는 0부터 생성하기 때문에 첫번째 인덱스 값을 -1 함
        arr_list = array[commands[i][0]-1:commands[i][1]]

        # 가져온 배열을 정렬함
        arr_list.sort()

        # 정렬된 데이터의 K번째 값 가져오기
        answer.append(arr_list[commands[i][2]-1])

    return answer