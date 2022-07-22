#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mam', 'dad', 'wife']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    [my_family[0], 165],
    [my_family[1], 180],
    [my_family[2], 168]
]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
def console_out(who):
    check = type(who)
    if check == list:
        print(who[0], '-', who[1], 'см')
    else:
        print('Error! "Who" is not list!')
    return

select = input('Введите индекс массива ')
if select == '0':
    console_out(my_family_height[0])
elif select == '1':
    console_out(my_family_height[1])
elif select == '2':
    console_out(my_family_height[2])
else:
    print('Error! Wrong index!')

# print(len(my_family_height))
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
count = family_high = 0
while count < len(my_family_height):
    family_high += my_family_height[count][1]
    count += 1

#   Общий рост моей семьи - ХХ см
print('Общий рост моей семьи =', family_high)