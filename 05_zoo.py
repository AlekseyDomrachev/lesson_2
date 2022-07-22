#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')
print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
count = 0
while count < len(zoo):
    # print(count)
    if zoo[count] == 'lion':
       print('Лев сидит в клетке № ', count)
    if zoo[count] == 'lark':
        print('Жаворонок сидит в клетке № ', count)
    count += 1
print('Удаляем 2й элемент списка...')
zoo.pop(2)
print(zoo)
count = 0
while count < len(zoo):
    # print(count)
    if zoo[count] == 'lion':
        print('Лев сидит в клетке № ', count)
    if zoo[count] == 'lark':
        print('Жаворонок сидит в клетке № ', count)
    count = count + 1


