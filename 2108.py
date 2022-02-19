import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

countLst = []
lst.sort()

# 산술평균
print(round(sum(lst) / n))


# 중앙값
print(lst[n//2])


# 최빈값
i = 0
while i < n:
    count = 1
    val = lst[i]

    for j in range(i+1, n, 1):
        if val == lst[j]:
            count += 1
        else:
            break
    i += count
    countLst.append([val, count])


countLst.sort(key=lambda x: (-x[1], x[0]))

if n == 1:
    print(countLst[0][0])
elif countLst[0][1] == countLst[1][1]:
    print(countLst[1][0])
else:
    print(countLst[0][0])

# 범위
print(max(lst) - min(lst))
