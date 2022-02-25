n, m = map(int, input().split(' '))

arr = []

# 중복 선택되지 않아야 하므로 사용되었는지 구별해주는 리스트 사용. False : 미방문, True : 방문
isUsed = [False] * (n+1)
isUsed[0] = True


def backTracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    else:
        for i in range(1, n+1):
            if isUsed[i] == False:
                # i가 이미 선택되었기 때문에 True 값으로 바꿔준다. 그리고 arr에 i를 append한다.
                isUsed[i] = True
                arr.append(i)

                # 재귀 호출로 만약 arr 길이가 m과 같다면 출력하면서 재귀 호출을 멈추고, 그렇지 않다면 계속 append 하는 작업이 반복된다.
                backTracking()

                # 한 세트를 완성하고 나서는 i 값을 False로 바꿔준다. 그 후 가장 최근에 들어온 값을 pop 해준다.
                isUsed[i] = False
                arr.pop()


backTracking()
