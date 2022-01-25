people = [[0]*15 for _ in range(15)]

for pp in range(1, 15):
    people[0][pp] = pp

for t in range(int(input())):
    floor = int(input())
    ho = int(input())
    sum = 0

    for i in range(0, floor+1):
        for j in range(1, ho+1):
            if people[i][j] == 0:   # 아직 값 저장 전
                for k in range(1, j+1):
                    people[i][j] += people[i-1][k]

    print(people[floor][ho])
