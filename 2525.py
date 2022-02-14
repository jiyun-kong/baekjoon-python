nowHour, nowMinute = map(int, input().split())
time = int(input())

total = nowHour*60 + nowMinute + time

hour = total // 60
minute = total % 60

if hour >= 24:
    hour = hour - 24
else:
    hour = hour

print(hour, minute)
