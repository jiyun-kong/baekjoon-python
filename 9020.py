# 소수 검정
lst = [False]*10001
lst[0] = True
lst[1] = True

for i in range(2, 10001):
    if lst[i] == False:
        for j in range(i*2, 10001, i):
            lst[j] = True


# 골드바흐 구하기
for t in range(int(input())):
    n = int(input())
    if n == 4:
        print("2 2")
    else:
        for i in range(n//2, 2, -1):
            if lst[i] == False and lst[n-i] == False:
                print(i, n-i)
                break
