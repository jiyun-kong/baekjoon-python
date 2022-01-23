num = int(input())


def denominator(num):
    n = 1

    while True:
        if n*(n+1) >= 2 * num:
            break
        else:
            n += 1

    if n % 2 == 0:      # 짝수라면 역방향
        return n - (num - (n-1)*(n)/2) + 1
    else:               # 홀수라면 정방향
        return num - (n-1)*(n)/2


def numerator(num):
    n = 1

    while True:
        if n*(n+1) >= 2 * num:
            break
        else:
            n += 1

    if n % 2 == 0:      # 짝수라면 정방향
        return num - (n-1)*(n)/2

    else:               # 홀수라면 역방향
        return n - (num - (n-1)*(n)/2) + 1


denom = denominator(num)    # 분모
numer = numerator(num)      # 분자

print("{}/{}".format(int(numer), int(denom)))
