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

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # запускает все тесты из документации


for num in range(174457, 174505+1):
    divisors = find_divisors(num)
    if len(divisors) == 2:  # если два делителя
        divisors.sort()  # сортируем
        print(f"{divisors[0]} {divisors[1]}")
