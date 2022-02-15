n = int(input())

i = 666
count = 0

while True:
    if '666' in str(i):
        count += 1
        if n == count:
            print(i)
            break
    i += 1
