dial = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], [
    'M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
str = list(input())
count = 0

for s in str:
    for dNum in range(len(dial)):
        if s in dial[dNum]:
            count += (dNum + 3)
            break

print(count)
