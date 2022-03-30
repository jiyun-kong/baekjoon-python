n = int(input())
drink = [0]
dp = [0]*(n+1)

for _ in range(n):
    drink.append(int(input()))

if n == 1:
    print(drink[1])
elif n == 2:
    dp[1] = drink[1]
    dp[2] = drink[1] + drink[2]

    print(dp[2])
elif n == 3:
    dp[1] = drink[1]
    dp[2] = drink[1] + drink[2]
    dp[3] = max(dp[1], drink[2] + dp[0]) + drink[3]

    print(max(dp))
else:
    dp[1] = drink[1]
    dp[2] = drink[1] + drink[2]
    dp[3] = max(dp[1], drink[2] + dp[0]) + drink[3]

    for i in range(4, n+1):
        dp[i] = max(dp[i-2], drink[i-1] + dp[i-3],
                    drink[i-1] + dp[i-4]) + drink[i]

    print(max(dp))
