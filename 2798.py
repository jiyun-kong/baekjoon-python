cardNum, goal = map(int, input().split())   # 카드 개수, 목표 숫자
card = list(map(int, input().split()))      # 카드 숫자 리스트
ok = []                                     # 가능한 합 리스트

card.sort()
for i in range(0, cardNum-2):
    for j in range(i+1, cardNum-1):
        for k in range(j+1, cardNum):
            sum = card[i] + card[j] + card[k]

            if sum <= goal:
                ok.append(sum)

            sum = 0

print(max(ok))
