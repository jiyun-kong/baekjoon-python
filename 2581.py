num1 = int(input())
num2 = int(input())
primeLst = []
isPrime = True

for n in range(num1, num2+1):
    if n == 1:
        isPrime = False
    else:
        i = 2
        isPrime = True

        while i < n:
            if n % i == 0:
                isPrime = False
                break
            else:
                i += 1

        if isPrime:
            primeLst.append(n)

if primeLst != []:
    print(sum(primeLst))
    print(min(primeLst))
else:
    print(-1)
