import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))

dp = [0]

if k == 1:
    print(max(lst))
elif k == n:
    print(sum(lst))
else:
    for i in lst:
        dp.append(dp[-1] + i)

    max = dp[k]

    for i in range(k+1, n+1):
        if max < dp[i] - dp[i-k]:
            max = dp[i] - dp[i-k]

    print(max)
