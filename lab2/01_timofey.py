
def timofey():
    """
    >>> timofey()
    10476
    """
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
    return k

def run_tests():
    import doctest
    res = doctest.testmod()
    if res.failed == 0:
        print ('\nВсе доктесты пройдены успешно')
    else:
        print ('\nДоктесты не пройдены где-то ошибка')

def main():
    run_tests()
    res = timofey()
    print(f"\nколичество различных кодов: {res}")

main()
