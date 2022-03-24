import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]    # 1번부터 n번까지의 index를 사용하기 위해서
dp = [0]*(n+1)

for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[1])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + stairs[i-1],
                    dp[i-2]) + stairs[i]

    print(dp[n])
