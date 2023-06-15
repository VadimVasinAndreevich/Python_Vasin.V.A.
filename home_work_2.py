# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

'''
import random
count_coin = int(input("Введите количество монет: "))
count = 1
count_coin_emblem = 0
count_coin_resko = 0
while count <= count_coin:
    coin = random.randint(0,1)
    if coin == 0:
        print('Монетка выпала гербом')
        count_coin_emblem += 1
    elif coin == 1:
        print('Монетка выпала решкой')
        count_coin_resko += 1
    count += 1
if(count_coin_emblem > count_coin_resko):
    turn_coin = count_coin - count_coin_emblem
    print(f'Нужно перевернуть монет: {turn_coin} - гербом')
elif(count_coin_emblem < count_coin_resko):
    turn_coin = count_coin - count_coin_resko
    print(f'Нужно перевернуть монет: {turn_coin} - решкой')
elif(count_coin_emblem == count_coin_resko):
    turn_coin = count_coin // 2
    print(f'Можно перевернуть монет: {turn_coin} - решкой, или {turn_coin} - гербом')
'''

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

'''
sum_number = int(input("Введите сумму чисел: "))
prod_number = int(input("Введите произведение чисел: "))
for x in range(0, 1000):
    for y in range(0, 1000):
        if(x + y == sum_number and x * y == prod_number):
            print(f'Загаданные числа {x} и {y}')
            break
'''

# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

'''
number = int(input("Введите число, ограничивающее значение при возведении в степень: "))
result = 2
k = 1
while result < number:
    result *= 2 
    print(k)
    k += 1
'''