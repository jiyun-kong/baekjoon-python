n = int(input())
count = 0

if n == 1:
    count = 1
else:
    i = -1
    middleSum = 2

    while True:
        i += 1
        if n > (middleSum + 6 * i):
            middleSum += 6 * i
            continue
        elif n == (middleSum + 6 * i):
            count = i + 2
            break
        else:
            count = i + 1
            break

print(count)
