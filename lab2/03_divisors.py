def find_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):  # проверяем до корня
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # если i не равно n // i, добавляем оба делителя
                divisors.append(n // i)
    return divisors

for num in range(174457, 174505+1):
    divisors = find_divisors(num)
    if len(divisors) == 2:  # если два делителя
        divisors.sort()  # сортируем
        print(f"{divisors[0]} {divisors[1]}")