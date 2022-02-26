n = int(input())
lst = list(map(int, input().split(' ')))
lst_premium = []

for i in range(n):
    lst_premium.append([i, lst[i]])

lst_premium.sort(key=lambda x: x[1])

for i in range(n-1):
    if i == 0:
        if lst_premium[i+1][1] > lst_premium[i][1]:
            lst_premium[i].append(0)
        elif lst_premium[i+1][1] == lst_premium[i][1]:
            lst_premium[i].append(0)
            lst_premium[i+1].append(0)

    else:
        if lst_premium[i+1][1] > lst_premium[i][1]:
            if len(lst_premium[i]) == 2:
                lst_premium[i].append(lst_premium[i-1][2] + 1)

        elif lst_premium[i+1][1] == lst_premium[i][1]:
            if len(lst_premium[i]) == 2:
                rank = lst_premium[i-1][2] + 1
                lst_premium[i].append(rank)
                lst_premium[i+1].append(rank)
            else:
                lst_premium[i+1].append(lst_premium[i][2])


if len(lst_premium) == 1:
    print(0)
else:
    if len(lst_premium[n-1]) == 2:
        lst_premium[n-1].append(lst_premium[n-2][2] + 1)

    lst_premium.sort(key=lambda x: x[0])
    print(' '.join(map(str, [lst_premium[i][2] for i in range(n)])))
