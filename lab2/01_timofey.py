import itertools


a = ['Т', 'И', 'М', 'О', 'Ф', 'Е', 'Й']
k = 0

for word in itertools.product(a, repeat=5):
    word = ''.join(word)

    if word.count('Й') > 1:  # Буква 'Й' не может повторяться
        continue
    if 'Й' in word:
        if word[0] == 'Й' or word[-1] == 'Й' or 'И' in word[word.index('Й') - 1:word.index('Й') + 2]:
            continue

    k += 1

print(f"количество различных кодов: {k}")
