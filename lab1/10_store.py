#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
# Стол
table_code = goods['Стол']
table_quantity_1 = store[table_code][0]['quantity']
table_price_1 = store[table_code][0]['price']
table_quantity_2 = store[table_code][1]['quantity']
table_price_2 = store[table_code][1]['price']
table_cost = (table_quantity_1 * table_price_1) + (table_quantity_2 * table_price_2)
table_quantity_total = table_quantity_1 + table_quantity_2
print('Стол -', table_quantity_total, 'шт, стоимость', table_cost, 'руб')

# Диван
sofa_code = goods['Диван']
sofa_quantity_1 = store[sofa_code][0]['quantity']
sofa_price_1 = store[sofa_code][0]['price']
sofa_quantity_2 = store[sofa_code][1]['quantity']
sofa_price_2 = store[sofa_code][1]['price']
sofa_cost = (sofa_quantity_1 * sofa_price_1) + (sofa_quantity_2 * sofa_price_2)
sofa_quantity_total = sofa_quantity_1 + sofa_quantity_2
print('Диван -', sofa_quantity_total, 'шт, стоимость', sofa_cost, 'руб')

# Стул
chair_code = goods['Стул']
chair_quantity_1 = store[chair_code][0]['quantity']
chair_price_1 = store[chair_code][0]['price']
chair_quantity_2 = store[chair_code][1]['quantity']
chair_price_2 = store[chair_code][1]['price']
chair_quantity_3 = store[chair_code][2]['quantity']
chair_price_3 = store[chair_code][2]['price']
chair_cost = (chair_quantity_1 * chair_price_1) + (chair_quantity_2 * chair_price_2) + (chair_quantity_3 * chair_price_3)
chair_quantity_total = chair_quantity_1 + chair_quantity_2 + chair_quantity_3
print('Стул -', chair_quantity_total, 'шт, стоимость', chair_cost, 'руб')

