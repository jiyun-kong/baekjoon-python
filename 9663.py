n = int(input())
lst = []          # 좌표들 저장하는 리스트
correct = []      # 완성된 좌표들 저장하는 리스트
count = 0         # 가능한 경우의 수
used = [[False for col in range(n)] for row in range(n)]    # 사용된 좌표인지 판단하는 리스트

for i in range(n):
    for j in range(n):
        lst.append([i, j])


def queens():
    if len(correct) == n:
        count += 1
    else:
        for posX, posY in lst:
            if used[posX][posY] == False:
                lst.append([posX, posY])
