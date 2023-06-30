# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

'''
first_el = int(input('Введите первый элемент массива: '))
diff_num = int(input('Введите разность элементов массива: '))
count_el = int(input('Введите количество элементов массива: '))
list_ar_prog = [first_el + (i - 1) * diff_num for i in range(1, count_el + 1)]
print(list_ar_prog)
'''

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# индексы: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 7 10
# Вывод: [1, 9, 13, 14, 19]

'''
task_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_mean_el = int(input('Введите минимальное значение диапазона: '))
max_mean_el = int(input('Введите максимальное значение диапазона: '))
index_list = [i for i in range(len(task_list)) if min_mean_el <= task_list[i] <= max_mean_el]
print(index_list)
'''