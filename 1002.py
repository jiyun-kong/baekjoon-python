for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    Rp = (r1 + r2) ** 2
    Rm = (r2 - r1) ** 2

    if dist == 0:
        if r1 != r2:
            print(0)
        else:
            print(-1)
    else:
        if Rm < dist and dist < Rp:
            print(2)
        elif Rp == dist:
            print(1)
        elif Rm == dist:
            print(1)
        elif Rp < dist:
            print(0)
        elif Rm > dist:
            print(0)
