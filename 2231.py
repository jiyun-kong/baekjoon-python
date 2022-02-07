n = int(input())
val = False
i = 1

while i < n:
    # 분해합이랑 n이랑 같아지면 그 때의 i 값이 생성자
    if i + sum(map(int, str(i))) == n:

        print(i)
        val = True
        break
    else:
        i += 1

if val == False:
    print(0)
