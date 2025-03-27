def find_divisors(n):
    """
    >>> find_divisors(6)
    [2, 3]
    >>> find_divisors(8)
    [2, 4]
    >>> find_divisors(17)
    []
    """
    divisors = []
    for i in range(2, int(n**0.5) + 1):  # проверяем до квадратного корня
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # если i не равно n // i, добавляем оба делителя
                divisors.append(n // i)
    return divisors

def run_tests():
    import doctest
    res = doctest.testmod()
    if res.failed == 0:
        print ('\nВсе доктесты пройдены успешно')
    else:
        print ('\nДоктесты не пройдены где-то ошибка')

def main():
    run_tests()
    print("\nЧисла с ровно двумя делителями в диапазоне 174457–174505:")  
    for num in range(174457, 174505 + 1):  
    # for num in range(5, 9):  
        divisors = find_divisors(num)  
        if len(divisors) == 2:  # если два делителя  
            print(f'Число {num}')
            print(f"{divisors[0]} {divisors[1]}")

main()
