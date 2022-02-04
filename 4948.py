n = int(input())

while n != 0:
    if n >= 2:
        lst = [False] * (2*n + 1)
        lst[0] = True
        lst[1] = True

        for i in range(2, 2*n+1):
            if lst[i] == False:
                for j in range(i*2, 2*n+1, i):
                    lst[j] = True

        lst = lst[n+1:]
        print(lst.count(False))
    else:
        print(1)
    n = int(input())
