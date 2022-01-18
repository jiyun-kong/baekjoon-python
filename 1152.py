str = list(input().split(' '))

if str[0] == '':
    del str[0]
if str[len(str)-1] == '':
    str.pop()

print(len(str))
