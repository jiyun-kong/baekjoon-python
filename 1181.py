word = []

for _ in range(int(input())):
    _word = input()
    word.append(_word)

word = set(word)
word = list(word)
word.sort()
word.sort(key=lambda x: len(x))

# sorted 함수는 출력할 당시까지만 순서대로 바꿔주는 함수임. sort를 써야지 순서대로 저장됨

print('\n'.join(map(str, word)))
