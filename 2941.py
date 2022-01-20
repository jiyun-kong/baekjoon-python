croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for cro_al in croatia:
    word = word.replace(cro_al, '*')

print(len(word))
