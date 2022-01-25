def apt(floor, ho):
    if floor == 0:
        return ho
    elif floor > 0:
        middleSum = 0
        for j in range(1, ho+1):        # 1층 ~ ho층까지 반복
            middleSum = middleSum + apt(floor-1, j)

        return middleSum


for t in range(int(input())):
    floor = int(input())
    ho = int(input())
    sum = 0

    for i in range(1, ho+1):
        sum = sum + apt(floor-1, i)

    print(sum)
