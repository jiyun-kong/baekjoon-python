import sys
input = sys.stdin.readline

n = int(input())  # n은 홀수
lst = []
countLst = []
maxLst = []

for _ in range(n):
    lst.append(int(input()))

# 산술평균
print(round(sum(lst) / n))


# 중앙값
lst.sort()
print(lst[n//2])


# 최빈값
i = 0
while True:
    if i >= n:
        break

    count = lst.count(lst[i])
    countLst.append((lst[i], count))
    i += count

sorted(countLst, key=lambda x: (x[0], -x[1]))

if len(countLst) == 1:
    print(countLst[0][0])
elif countLst[0][1] == countLst[1][1]:
    print(countLst[1][0])
else:
    print(countLst[0][0])

# 범위
print(max(lst) - min(lst))
