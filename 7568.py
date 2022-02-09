lst = []
rank = []

for i in range(int(input())):
    info = tuple(map(int, input().split()))
    lst.append(info)

for i in range(len(lst)):
    count = 0

    for j in range(len(lst)):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            count += 1
    rank.append(count + 1)

for i in range(len(rank)):
    print(rank[i], end=" ")
