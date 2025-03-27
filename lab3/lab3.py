# рекурсивная

def count(x):
    k = 0
    for item in x:
        if isinstance(item, list):  # если список вызываем функцию 
            k += count(item) + 1
        else:
            k += 1  
    return k

# не  рекурсивная

def count2(x):
    k = 0
    while x:
        item = x.pop(0)  # извлекаем первый item 
        if isinstance(item, list):  
            x = item + x 
            k += 1  
        else:
            k += 1 
    return k


# примеры
print(count([]))  # 0
print(count([1, 2, 3]))  # 3
print(count(["x", "y", ["z"]]))  # 4
print(count([1, 2, [3, 4, [5]]]))  #  7

print(count2([]))  # 0
print(count2([1, 2, 3]))  # 3
print(count2(["x", "y", ["z"]]))  # 4
print(count2([1, 2, [3, 4, [5]]]))  #  7



# рекурсивная

def calc(n):
    if n == 1:
        return 1
    if n == 2:
        return -1 / 8
    x_1 = calc(n - 1)
    x_2 = calc(n - 2)
    return ((n - 1) * x_1) / 3 + ((n - 2) * x_2) / 4

n = int(input("Введите n для рекурсии: "))
for i in range(1, n + 1):
    print(f"x[{i}] = {calc(i)}")

# не рекурсивная

def calc2(n):
    # список для хранения 
    values = [0] * (n + 1)
    
    values[1] = 1
    if n >= 2:
        values[2] = -1 / 8
    
    # заполняем список значениями для всех n > 2
    for i in range(3, n + 1):
        values[i] = ((i - 1) * values[i - 1]) / 3 + ((i - 2) * values[i - 2]) / 4
    
    for i in range(1, n + 1):
        print(f"x[{i}] = {values[i]}")

# вводим n и выводим 
n = int(input("Введите n для не рекурс функции: "))
calc2(n)
