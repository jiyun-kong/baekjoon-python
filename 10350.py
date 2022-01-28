for t in range(int(input())):
    floor, room, th = map(int, input().split())
    c = h = 0

    if th % floor == 0:
        c = floor
        h = th // floor
    else:
        c = th % floor           # 층 수
        h = th // floor + 1       # 호 수

    if h <= 9:
        print("{}0{}".format(c, h))
    else:
        print("{}{}".format(c, h))
