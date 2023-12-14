import db_rw
import Controller
import datetime

# Чтение контактов из базы
db_rw.readDB()

# Основное меню
choice=0
while True:
    print('Добро пожаловать в основное меню заметок.\n'
    'Варианты работы с заметками:\n'
    '1 - вывод всех заметок. '
    '2 - добавляем заметку. '
    '3 - изменяем заметку.\n'
    '4 - удаляем заметку по id. '
    '5 - сохраняем изменения в базу и выходим')
    try:
        choice = int(input(f'Ваш выбор: '))
    except ValueError:
        print("Вы ввели не число. Попробуйте снова.")
    else:
        if (choice < 1) or (choice > 5):
            print("Здесь нет такой операции.")

# Вывод всех заметок
    if choice == 1:
        Controller.Print()

# Добавление новую заметку
    if choice == 2:
        subject = str(input(f'Введите заголовок: '))
        text = str(input(f'Введите текст заметки: '))
        datetimeNow = datetime.datetime.now()
        Controller.Add(subject, text, datetimeNow)

# Изменение заметки
    if choice == 3:
        id = int(input(f'Введите номер заметки для изменения: '))
        Controller.PrintOne(id)
        print('\n')

        subject = str(input(f'Введите новый заголовок: '))
        text = str(input(f'Введите новый текст заметки: '))
        datetimeNow = datetime.datetime.now()
        Controller.Change(id, subject, text, datetimeNow)

    # Удаление заметки
    if choice == 4:
        id = int(input(f'Введите номер заметки для удаления: '))
        Controller.Erase(id)  

# Выход и запись заметок
    if choice == 5:
        db_rw.writer()
        break