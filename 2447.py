num = int(input())

power = 0
while num // 3 != 0:
    num = num // 3
    power += 1

print(power)
