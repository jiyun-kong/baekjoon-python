import math

up, down, height = map(int, input().split())
day = 0
day = math.ceil((height - up) / (up - down)) + 1

print(day)
