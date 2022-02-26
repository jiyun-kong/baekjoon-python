n = int(input())
lst = list(map(int, input().split(' ')))

# set으로 중복 제거하고 list로 만들어서 sort로 오름차순 정렬
lst2 = list(set(lst))
lst2.sort()

# lst2의 값을 key 값으로 하고, 인덱스 값을 value로 하는 dictionary 만들기
dict = {lst2[i]: i for i in range(len(lst2))}

for ele in lst:
    print(dict[ele], end=' ')
