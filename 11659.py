import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
dp = [0]

for i in (lst):
    dp.append(dp[-1] + i)


for _ in range(m):
    i, j = map(int, input().split(' '))
    print(dp[j] - dp[i-1])
