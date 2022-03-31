import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split(' ')))
dp = [[] for _ in range(n)]

if n == 1:
    print(1)
else:
    for i in range(n):
        dp[i].append(seq[i])

        for j in range(i+1, n):
            if dp[i][-1] < seq[j]:
                dp[i].append(seq[j])
    # print(dp)
    max = 1
    for i in range(n):
        if max < len(dp[i]):
            max = len(dp[i])

    print(max)

# 반례 : n = 6 / 1 2 8 2 4 8
