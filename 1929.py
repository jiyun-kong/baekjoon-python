num1, num2 = map(int, input().split())

# True : 이미 지워진 값, False : 지워지지 않은 값
numLst = [False] * (num2+1)
numLst[0] = True
numLst[1] = True

for i in range(2, num2+1):
    if numLst[i]:
        continue

    for j in range(i*2, num2+1, i):
        numLst[j] = True


for i in range(num1, num2+1):
    if not numLst[i]:
        print(i)
