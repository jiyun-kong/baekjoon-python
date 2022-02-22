coordinate = []

for i in range(int(input())):
    coordinate.append(list(map(int, input().split(' '))))

coordinate.sort(key=lambda x: (x[1], x[0]))

for co in coordinate:
    print(co[0], co[1])
