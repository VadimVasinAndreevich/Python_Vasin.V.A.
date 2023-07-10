def input_user_data():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    adress = input('Введите адрес: ')
    return name, surname, phone, adress

def input_user_delete():
    id = input('Введите id человека, данные которого нужно удалить: ')
    return id

def input_user_change():
    print('Введите данные, которые хотите изменить, если данные изменять не нужно поставьте "-"')
    name = input('Введите изменённое имя: ')
    surname = input('Введите изменённую фамилию: ')
    phone = input('Введите изменённый телефон: ')
    adress = input('Введите изменённый адрес: ')
    return name, surname, phone, adress