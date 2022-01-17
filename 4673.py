selfNum = [False] * 10001

for i in range(1, 10001):
    res = i

    while i//10 != 0:
        res += i % 10
        i //= 10

    res += i

    if res <= 10000:
        selfNum[res] = True

for j in range(1, 10001):
    if selfNum[j] == False:
        print(j)
