import sys
input = sys.stdin.readline

n = int(input())  # n은 홀수
lst = []
countLst = []
maxLst = []

for _ in range(n):
    lst.append(int(input()))

# # 산술평균
# print(round(sum(lst) / n))

# # 중앙값
# lst.sort()
# print(lst[n//2])

# 최빈값
for i in range(n):
    count = lst.count(lst[i])
    countLst.append((lst[i], count))
print("countLst : ", countLst)
max = 0
for j in range(len(countLst)):
    if max < countLst[j][1]:
        max = countLst[j][1]
        maxElement = countLst[j][0]

        if maxElement not in maxLst:
            maxLst.append(maxElement)
print("before sorting maxLst : ", maxLst)
maxLst.sort(reverse=True)
print("after sorting maxLst : ", maxLst)

if len(maxLst) > 1:
    print(maxLst[1])
else:
    print(maxLst[0])

# # 범위
# print(max(lst) - min(lst))
