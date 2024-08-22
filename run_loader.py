"""
Модуль-программа импорта csv файлов в базу данных (загрузчик csv).
"""

# --------------------------------
from tkinter import *

# --------------------------------
from methods.btns import *



root = Tk()

# https://github.com/ArtemXYZ/csv_loader.git



# ------------------------------- Настройки главного окна
root['bg'] = '#96CDCD'  # Указываем фоновый цвет (изменить на другой или добавить фон)
root.title('CSVLoader')  # Указываем название окна
root.geometry('600x500')  # Указываем размеры окна

# todo добавить иконку программе

root.resizable(width=False, height=False)  # Делаем невозможным менять размеры окна


# ------------------------------- Создаем фрейм (область для размещения других объектов)

# # Указываем к какому окну он принадлежит, какой у него фон и какая обводка
# frame_top = Frame(root, bg='#FFDAB9', bd=15)
# frame_top.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3) # Также указываем его расположение


# Заглавная лейба
frame_top = Frame(root, bg='#FFDAB9', bd=15)
frame_top.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1) # Также указываем его расположение


# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(root, bg='#FFDAB9', bd=15)
frame_top.place(relx=0.05, rely=0.17, relwidth=0.35, relheight=0.15) # Также указываем его расположение

#
# # Текстовая надпись в окне параметров подключения:
# label_param_url_engine = Label(frame_top, text='Заполните параметры подключения к базе данных', font=40)
# label_param_url_engine.pack()  # grid() place()

# # Текстовая надпись: Введите
# label_param_url_engine = Label(frame_top, text='Диалект базы данных', font=2)
# label_param_url_engine.pack()  # grid() place()


# Создаем текстовое поле для получения данных от пользователя
write_db = Entry(frame_top, bg='#7CCD7C', font=10)
write_db.pack() # Размещение этого объекта, всегда нужно прописывать


# # Все то-же самое, но для второго фрейма
# frame_bottom = Frame(root, bg='#ffb700', bd=5)
# frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
#
#
#
# # Создаем текстовое поле для получения данных от пользователя
# cityField = Entry(frame_top, bg='#7CCD7C', font=30)
# cityField.pack() # Размещение этого объекта, всегда нужно прописывать
#
# # Создаем кнопку и при нажатии будет срабатывать метод "?"
# btn = Button(frame_top, text='Выбрать папку', command=open_folder)
# btn.pack()
#
# # Создаем текстовую надпись, в которую будет выводиться информация о погоде
# info = Label(frame_bottom, text='Результат выполнения запроса на апдейт', bg='#7CCD7C', font=40)
# info.pack()

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()