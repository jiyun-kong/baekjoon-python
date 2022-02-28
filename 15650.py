n, m = map(int, input().split(' '))

used = [False] * (n+1)
used[0] = True
arr = []


def nm():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    else:
        for i in range(1, n+1):
            if used[i] == False:
                used[i] = True
                arr.append(i)
                nm()
                arr.pop()


nm()
