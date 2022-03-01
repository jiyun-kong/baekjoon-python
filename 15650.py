n, m = map(int, input().split(' '))

arr = []


def nm(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
    else:
        for i in range(start, n+1):
            if i not in arr:
                arr.append(i)
                print("arr : ", arr, "\tstart : ", start, "\ti : ", i)
                print("nm(", i+1, ")")
                nm(i + 1)
                arr.pop()
                print("pop()")


start = 1
nm(start)
