import sys

lst = []
input = sys.stdin.readline

for nn in range(int(input())):
    lst.append(int(input()))

lst.sort()

for i in range(len(lst)):
    print(lst[i])
