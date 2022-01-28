n = int(input())

if n >= 1:
    nn = 2
    while nn <= n:
        while n % nn == 0:
            print(nn)
            n = n // nn
        nn += 1
