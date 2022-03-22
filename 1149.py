n = int(input())
rgb = []

for i in range(n):
    lst = list(map(int, input().split(' ')))
    rgb.append(lst)

for i in range(1, n):
    # R
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]

    # G
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]

    # B
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[n-1]))
