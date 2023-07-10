from data_create import input_user_data, input_user_delete, input_user_change


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress};\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
        id = str((len(data)-1) // 6 + 1)
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{id}\n'
                       f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
        id = str((len(data)-1) // 2 + 1)
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{id};{name};{surname};{phone};{adress};\n\n')

    print(f'Данные добавлены в {var} файл')


def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))

    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(''.join(data))

def delete_data():
    var = int(input('Из какого файла удалить данные (1 или 2): '))
    if var > 2 or var < 1:
        print('Такого файла не существует, введите ещё раз')
        return delete_data()
    id = input_user_delete()

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
        for i in range(len(data)-1):
            if data[i] == f'{id}\n':
                j = i
                while i <= j+5:
                    if i != len(data)-1:
                        data[i] = 'del'
                        i+=1
                    elif i == len(data)-1:
                        break
        new_data = [data[i] for i in range(len(data)-1) if data[i] != 'del']
        j = 0
        for i in range(len(new_data)-1):
            if i % 6 == 0 and i // 6 >= int(id):
                new_data[i] = f'{int(id)+j}\n'
                j += 1
        new_data.append('\n')
        if (len(new_data)-1) % 6 == 0:
            res = new_data.pop(len(new_data)-1)
            del(res)
        print(new_data)  
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(new_data)

    elif var == 2:       
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = (file.read()).split(';')
        for i in range(len(data)-1):
            if i == int(id)*5:
                data[i+1] = 'del'
                data[i+2] = 'del'
                data[i+3] = 'del'
                data[i+4] = 'del'
                data[i+5] = 'del'
        new_data = [data[i] for i in range(len(data)-1) if data[i] != 'del']
        for i in range(len(new_data)-1):
            if i == 0:
                new_data[i] == '0'
            elif i % 5 == 0 and i != 0 and i // 5 > int(id):
                new_data[i] = f'\n\n{i//5}'
        new_data.append('\n\n')
        new_data = ';'.join(new_data)
        print(new_data)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(new_data)
        
    print(f'Данные человека с id - {id} удалены из файла {var}')    

def change_data():
    var = int(input('В какой файл внести изменённые данные (1 или 2)? '))
    if var > 2 or var < 1:
        print('Такого файла не существует, введите ещё раз')
        return change_data()
    name, surname, phone, adress = input_user_change()
    id = input('Введите id человека, которому нужно внести изменения: ')
    
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data = file.readlines()
        for i in range(len(data)-1):
                if data[i] == f'{id}\n':
                    if name != '-':
                        data[i+1] = f'{name}\n'
                    if surname != '-':
                        data[i+2] = f'{surname}\n'
                    if phone != '-':
                        data[i+3] = f'{phone}\n'
                    if adress != '-':
                        data[i+4] = f'{adress}\n'
                    break
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(data)

    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data = (file.read()).split(';')
        for i in range(len(data)-1):
                if i == int(id)*5:
                    if name != '-':
                        data[i+1] = f'{name}'
                    if surname != '-':
                        data[i+2] = f'{surname}'
                    if phone != '-':
                        data[i+3] = f'{phone}'
                    if adress != '-':
                        data[i+4] = f'{adress}'
                    break
        data = ';'.join(data)
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(data) 

    print(f'В данные человека с id - {id} внесены изменения в файл {var}')