n, m = map(int, input().split(' '))

arr = []


def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    else:
        for i in range(1, n+1):
            if i not in arr:
                arr.append(i)
                dfs()
                arr.pop()


dfs()
