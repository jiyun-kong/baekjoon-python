operLst = []    # 연산자 저장 리스트
arr = []
resLst = []     # 결과값 저장 리스트
oper = ['+', '-', '*', '//']

n = int(input())    # 숫자 개수
numLst = list(map(int, input().split(' ')))
operNum = list(map(int, input().split(' ')))
isUsed = [False] * (n-1)

for i in range(len(operNum)):
    for o in range(operNum[i]):
        operLst.append(oper[i])


def dfs(start):
    if len(arr) == 2*n-2:
        arr.append(numLst[-1])
        print(arr)
        # 결과값 저장하기

    else:
        for i in range(start, n-1):
            arr.append(numLst[i])
            if isUsed[i] == False:
                arr.append(operLst[i])
                isUsed[i] = True
                print(arr)
                dfs(i+1)
                isUsed[i] = False
                arr.pop()
                arr.pop()
                print(arr)


dfs(0)
