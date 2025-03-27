
def count_ones():
    """
    >>> count_ones()
    2015
    """
    res = bin(4**2020 + 2**2017 - 15)
    k = res.count('1')
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
    res = count_ones()
    print(f"\nКоличество единиц в двоичной записи: {res}")

main()
