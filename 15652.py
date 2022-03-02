n, m = map(int, input().split(' '))
arr = []


def nm(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    else:
        for i in range(start, n+1):
            arr.append(i)
            nm(i)
            arr.pop()


nm(1)
