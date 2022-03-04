n = int(input())

arr = [0]*n
ans = 0         # 가능한 경우의 수


def isOkay(col):
    for i in range(col):
        if abs(arr[i] - arr[col]) == abs(i - col) or arr[i] == arr[col]:
            return False

    return True


def queens(col):
    global ans
    if col == n:
        ans += 1
    else:
        for i in range(n):
            arr[col] = i

            if isOkay(col):
                queens(col+1)


queens(0)
print(ans)
