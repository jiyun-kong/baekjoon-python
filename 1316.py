testCase = int(input())
count = 0

for t in range(testCase):
    _str = list(input())
    res = True                  # True : 기본값 / False : 그룹 단어가 아님

    i = 0

    while True:
        last_idx = len(_str) - 1

        if i == last_idx:
            break
        else:
            if _str[i] == _str[i+1]:
                del _str[i]
            else:
                i += 1

    for k in range(len(_str)-1):
        for j in range(k+1, len(_str)):
            if _str[k] == _str[j]:
                res = False
                break

    if res == True:
        count += 1

print(count)
