a = b = c = 0
dp = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return dp[20][20][20]
    elif a < b and b < c:
        return dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
    else:
        return dp[a-1][b][c]+dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]


for i in range(21):
    for j in range(21):
        for k in range(21):
            if dp[i][j][k] == 0:
                dp[i][j][k] = w(i, j, k)

while True:
    a, b, c = map(int, input().split(' '))

    if a == -1 and b == -1 and c == -1:
        break
    else:
        print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))
