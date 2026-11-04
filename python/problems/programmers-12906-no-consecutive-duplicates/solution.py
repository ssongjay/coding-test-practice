def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(0, len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if tmp == arr[i]:
                continue
            else:
                answer.append(arr[i])
        tmp = arr[i]
    return answer
