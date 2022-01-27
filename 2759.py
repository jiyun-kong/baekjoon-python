numLst = []

for i in range(int(input())):
    numLst.append(int(input()))

numLst.sort()

for j in range(len(numLst)):
    print(numLst[j])
