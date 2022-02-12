saero, garo = map(int, input().split())
lst = []            # 입력된 보드의 상태를 저장하는 리스트
errorStorage = []   # 몇 개의 원소를 고쳐야 하는지 저장하는 리스트 -> 나중에 min(errorStorage)

# 입력받기
for i in range(saero):
    lst.append(input())

# 검토하기
for i in range(0, saero-7):
    for j in range(0, garo-7):
        count = 0

        for y in range(i, i+8):
            for x in range(j, j+8):
                if (y-i) % 2 == 0:
                    if (x-j) % 2 == 0:
                        if lst[y][x] == 'B':
                            count += 1
                    else:
                        if lst[y][x] == 'W':
                            count += 1
                else:
                    if (x-j) % 2 == 0:
                        if lst[y][x] == 'W':
                            count += 1
                    else:
                        if lst[y][x] == 'B':
                            count += 1
        errorStorage.append(count)

        count = 0
        for y in range(i, i+8):
            for x in range(j, j+8):
                if (y-i) % 2 == 0:
                    if (x-j) % 2 == 0:
                        if lst[y][x] == 'W':
                            count += 1
                    else:
                        if lst[y][x] == 'B':
                            count += 1
                else:
                    if (x-j) % 2 == 0:
                        if lst[y][x] == 'B':
                            count += 1
                    else:
                        if lst[y][x] == 'W':
                            count += 1
        errorStorage.append(count)

print(min(errorStorage))
