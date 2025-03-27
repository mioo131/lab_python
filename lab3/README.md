# Отчет по решению задач лабараторной работы № 3

## 1. Функция для подсчёта числа элементов в списках, включая вложенные списки

**Решение:**

Написал функцию count, которая:

1. Проверяется, является ли текущий элемент вложенным списком. - вызывается функция count рекурсивно и добавляет + 1
2. Если элемент не является списком, увеличивается общий счётчик.

```python
def count(x):
    k = 0
    for item in x:
        if isinstance(item, list):  # Если элемент — список, вызываем функцию рекурсивно
            k += count(item) + 1
        else:
            k += 1  # Если элемент — не список, увеличиваем счётчик
    return k
```

**Решение без рекурсии:**

```python
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
```

**Результат:**

![img_1.png](img_1.png)

--- 

## 2. Функция для расчёта

Формула расчёта последовательности:

![formula](https://latex.codecogs.com/png.latex?x_i%20%3D%20%5Cfrac%7B%28i-1%29x_%7Bi-1%7D%7D%7B3%7D%20%2B%20%5Cfrac%7B%28i-2%29x_%7Bi-2%7D%7D%7B4%7D)

Где:
- x_1 = 1
- x_2 = -1/8

**Решение:**

Функция `calc`:
1. Если n является 1 или 2, то передает значения указанные в задании
2. Остальное считатется по формуле 

n вводится с клавиатуры и через цикл выводит значения функции от 1 до n

```python
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
```
**Решение без рекурсии:**

```python
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
 
```


**Результат:**

![img.png](img.png)

---

## Список используемых источников:

[списки python](https://skillbox.ru/media/code/spiski-v-python-chto-eto-takoe-i-kak-s-nimi-rabotat/)

[hекурсия функции](https://skillbox.ru/media/code/kak-rabotaet-rekursiya-funktsii-obyasnyaem-na-primere-python/)

[Python tutorial](https://docs.python.org/3/tutorial/)
