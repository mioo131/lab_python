def count(x):
    k = 0
    for item in x:
        if isinstance(item, list):  # Если элемент — список, вызываем функцию рекурсивно
            k += count(item) + 1
        else:
            k += 1  # Если элемент — не список, увеличиваем счётчик
    return k

# Примеры
print(count([]))  # Ожидается 0
print(count([1, 2, 3]))  # Ожидается 3
print(count(["x", "y", ["z"]]))  # Ожидается 4
print(count([1, 2, [3, 4, [5]]]))  # Ожидается 7


def calc(n):
    if n == 1:
        return 1
    if n == 2:
        return -1 / 8
    x_1 = calc(n - 1)
    x_2 = calc(n - 2)
    return ((n - 1) * x_1) / 3 + ((n - 2) * x_2) / 4

n = int(input("Введите n: "))
for i in range(1, n + 1):
    print(f"x[{i}] = {calc(i)}")
