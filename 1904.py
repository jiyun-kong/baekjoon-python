import sys
input = sys.stdin.readline
n = int(input())

arr = [0]*1000001

arr[1] = 1
arr[2] = 2

if n >= 3:
    for i in range(3, n+1):
        count = arr[i-2] + arr[i-1]

        arr[i] = count % 15746

print(arr[n])
