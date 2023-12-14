import Notebook
import db_rw

# Вывод всех контактов
def Print():
    for row in db_rw.my_list:
        print("%2d" %(db_rw.my_list.index(row) +1), end=' ')
        Notebook.Notebook.display_notebook(row)

# Удаление контакта
def Erase(id):
    print('Удалена запись:')
    Notebook.Notebook.display_notebook(db_rw.my_list[id-1])
    db_rw.my_list.pop(id-1)
    print('\n')

# Добавление контакта
def Add(subject, text, datetimeNow):
    db_rw.my_list.append(Notebook.Notebook(subject, text, datetimeNow))
    print('Добавлена запись:')
    Notebook.Notebook.display_notebook(db_rw.my_list[-1])
    print('\n')

# Вывод одной заметки
def PrintOne(id):
    Notebook.Notebook.display_notebook(db_rw.my_list[id-1])

# Изменение контакта
def Change(id, subject, text, datetimeNow):
    db_rw.my_list.insert(id-1, Notebook.Notebook(subject, text, datetimeNow))
    db_rw.my_list.pop(id)
    print('Запись изменена!')
    print('\n')



