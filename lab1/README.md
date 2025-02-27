# Отчет по выполнению заданий

## Описание проделанной работы
1. Скачан архив с заданиями и распакован в репозиторий.
4. Протестированы результаты выполнения каждого задания.
5. В репозиторий добавлены все коды и отчет.

##  Задание 00
Составить словарь словарей и найти расстояние между городами.

## # Описание 
Составил словарь словарей и нашел расстояние между ними.

###  Решение
```
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = {
    'Moscow => London': (((550 - 510) ** 2 + (370 - 510) ** 2) ** 0.5),
    'London => Paris': (((510 - 480) ** 2 + (510 - 480) ** 2) ** 0.5),
    'Paris => Moscow': (((480 - 550) ** 2 + (480 - 370) ** 2) ** 0.5),
}

print(distances)
```
## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/0.png?raw=true)

# Задание 01

## Описание
Нашел площадь круга, определил лежит ли точка внутри того самого круга.

## Решение
```
radius = 42
pi=3.1415926
print("радиус - ",pi*radius**2)

point_1 = (23, 34)
print((point_1[0]**2+point_1[1]**2)**0.5<radius)

point_2 = (30, 30)
print((point_2[0]**2+point_2[1]**2)**0.5<radius)

```

## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/01.png?raw=true)

# Задание 02
Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, что бы получилось число "25".

## Описание
Расставил знаки операций между цифрами 1 2 3 4 5, чтобы получить число 25.

## Решение
```
print(((1+2)*3-4)*5)

```

## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/02.png?raw=true)

# Задание 03
Выведите на консоль с помощью индексации строки, последовательно:
   первый фильм
   последний
   второй
   второй с конца
## Описание
Используя срезы, вывела на консоль название фильмов.
## Решение
```
print(my_favorite_movies[:10])
print(my_favorite_movies[-15:])
print(my_favorite_movies[12:25])
print(my_favorite_movies[-22:-17])
```
## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/03.png?raw=true)
# Задание 04
Создайте списки, выведите на консоль рост отца и общий рост всей семьи.
## Описание
Составила список приблизительного роста членов моей семьи, вывела на консоль рост отца и общий рост семьи.
## Решение
```
my_family = ['мама', 'папа', 'дедушка', 'бабушка']
my_family_height = [ 
    # ['имя', рост],
    ['мама',170],['папа',180],['бабушка',160],['дедушка',165],
]
summ= my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
print("Рост отца -", my_family_height[1][1])
print("Общий рост семьи -", summ)
```
## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/04.png?raw=true)

# Задание 05
посадите медведя (bear) между львом и кенгуру,добавьте птиц из списка birds в последние клетки зоопарка,уберите слона,в какой клетке сидит лев (lion) и жаворонок (lark).
Номера при выводе должны быть понятны простому человеку, не программисту.
## Описание
Использовала функции для добавления, удаления животных в клетки.
## Решение
```
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1,'bear')
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)

zoo.remove('elephant')
print(zoo)

print("Лев -", zoo.index('lion') + 1)
print("Жаворонок -", zoo.index('lark') + 1)
```

## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/05.png?raw=true)

# Задание 06
распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
Три песни звучат ХХХ.XX минут
распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
А другие три песни звучат ХХХ минут

## Описание
Расчитала общее время звучания трех песен 'Halo', 'Enjoy the Silence' и 'Clean' и 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'.

## Решение
```
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

x = round(violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[-1][1],2)
print("Три песни звучат",x ,"минут")

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

y = round(violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth'] + violator_songs_dict['Blue Dress'],2)
print("А другие три песни звуечат",y ,"минут")
```

## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/06.png?raw=true)
# Задание 07

## Описание
Составила с помощью срезов предложение по буквам .
## Решение
```
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
let1 = secret_message[0][3]
let2 = secret_message[1][9:13]
let3 = secret_message[2][5:15:2]
let4 = secret_message[3][12:6:-1]
let5 = secret_message[4][20:15:-1]
print(let1, let2, let3, let4, let5)
```
## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/07.png?raw=true)


# Задание 08
создайте множество цветов, произрастающих в саду и на лугу,выведите на консоль все виды цветов,выведите на консоль те, которые растут и там и там,выведите на консоль те, которые растут в саду, но не растут на лугу,выведите на консоль те, которые растут на лугу, но не растут в саду
## Описание
Создала множество цветов, вывела все виды, повторяющиеся цветы и те, что растут на одном месте, но не растут на другом.
## Решение
```
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)

print(garden_set | meadow_set)
print(garden_set & meadow_set)
print(garden_set.difference(meadow_set))
print(meadow_set.difference(garden_set))
```
## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/08.png?raw=true)


# Задание 09
Создайте словарь цен на продкты следующего вида (писать прямо в коде),указать надо только по 2 магазина с минимальными ценами
## Описание
Создала словарь цен на печенье, конфеты, карамель, пирожное с минимальными ценами.
## Решение
```
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99}
        
        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
    ],
    'конфеты': [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99}
    ],
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
    'карамель': [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99}
    ],
    'пирожное': [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99}
    ]
}

print(sweets)
```

## Скриншот
![](https://github.com/Agmongui/python/blob/main/lab01/09.png?raw=true)

## Шпаргалка по работе с командами git

1. Сlone <URL репозитория> - Клонировать репозиторий на локальную машину
2. Commit — фиксирует изменения.
3. Push — отправляет изменения на сервер.
4. Pull — скачивает обновления с сервера.

