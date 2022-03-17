n = int(input())
rgb = []

for i in range(n):
    lst = list(map(int, input().split(' ')))
    rgb.append(lst)

print(rgb)
