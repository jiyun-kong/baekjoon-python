saero, garo = map(int, input().split())
lst = []            # 입력된 보드의 상태를 저장하는 리스트
errorStorage = []   # 몇 개의 원소를 고쳐야 하는지 저장하는 리스트
idx = 0             # wb 리스트를 확인 할 인덱스

wb = ['w', 'b']

# 입력받기
for i in range(saero):
    lst.append(input())

for i in range(0, saero-7):
    for j in range(0, garo-7):
