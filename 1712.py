a, b, c = map(int, input().split())


def breakEvenPoint(start, end, a, cb):
    middle = (start + end) // 2

    if start > end:
        return middle+1

    if cb * middle > a:
        return breakEvenPoint(start, middle-1, a, cb)
    elif cb * middle == a:
        return middle + 1
    else:
        return breakEvenPoint(middle+1, end, a, cb)


if c - b <= 0:
    count = -1
else:
    count = breakEvenPoint(1, a, a, c-b)


print(count)
