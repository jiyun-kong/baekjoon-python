fibo_zeroOne = []
fibo = [False]*41

fibo_zeroOne.append([1, 0])
fibo_zeroOne.append([0, 1])

fibo[0] = True
fibo[1] = True

for _ in range(int(input())):
    n = int(input())

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    elif n >= 2:
        for i in range(2, n+1):
            if fibo[i] == False:
                fibo_zeroOne.append(
                    [fibo_zeroOne[i-2][0] + fibo_zeroOne[i-1][0], fibo_zeroOne[i-2][1] + fibo_zeroOne[i-1][1]])
                fibo[i] = True

        print(fibo_zeroOne[n][0], fibo_zeroOne[n][1])
print(fibo_zeroOne)
print(fibo)
