"""
Модуль-программа импорта csv файлов в базу данных (загрузчик csv).
"""

# --------------------------------
from tkinter import *



# --------------------------------
# from methods.btns import
from methods.to_csv import convert_to_csv
from methods.file_open import select_file, choose_destination


from tkinter import StringVar, messagebox


# Создаем главное окно приложения
# root = tk.Tk()

# https://github.com/ArtemXYZ/csv_loader.git



# ------------------------------- Настройки главного окна
# root['bg'] = '#96CDCD'  # Указываем фоновый цвет (изменить на другой или добавить фон)
# root.title('CSVLoader')  # Указываем название окна
# root.geometry('600x500')  # Указываем размеры окна

# todo добавить иконку программе

# root.resizable(width=False, height=False)  # Делаем невозможным менять размеры окна
#
# canvas = Canvas(root, height=600, width=500)
# canvas.pack()




# ------------------------------- Создаем фрейм (область для размещения других объектов)

# # Указываем к какому окну он принадлежит, какой у него фон и какая обводка
# frame_top = Frame(root, bg='#FFDAB9', bd=15)
# frame_top.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3) # Также указываем его расположение


# Заглавная лейба
# frame_top = Frame(root, bg='#FFDAB9', bd=15)
# frame_top.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1) # Также указываем его расположение +
#
#
# # Указываем к какому окну он принадлежит, какой у него фон и какая обводка
# frame_top = Frame(root, bg='#FFDAB9', bd=15)
# frame_top.place(relx=0.05, rely=0.17, relwidth=0.35, relheight=0.15) # Также указываем его расположение +

#
# # Текстовая надпись в окне параметров подключения:
# label_param_url_engine = Label(frame_top, text='Заполните параметры подключения к базе данных', font=40)
# label_param_url_engine.pack()  # grid() place()

# # Текстовая надпись: Введите
# label_param_url_engine = Label(frame_top, text='Диалект базы данных', font=2) +
# label_param_url_engine.pack()  # grid() place()


# # Создаем текстовое поле для получения данных от пользователя +
# write_db = Entry(frame_top, bg='#7CCD7C', font=10)
# write_db.pack() # Размещение этого объекта, всегда нужно прописывать


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

# ----------------------------------------------------------------------------------------------------------------------

# # Функция для создания поля с надписью, границей и связанной переменной
# def create_labeled_entry(root, label_text, row, column, width=30, colspan=1, show=None):
#     frame = tk.Frame(root, bd=1, relief="solid", bg=root['bg'])
#     frame.grid(row=row, column=column, padx=15, pady=7, sticky="w", columnspan=colspan)
#
#     label = tk.Label(frame, text=label_text, anchor="w", bg=root['bg'])
#     label.grid(row=0, column=0, sticky="w")
#
#     var = tk.StringVar()
#     entry = tk.Entry(frame, textvariable=var, width=width, show=show)
#     entry.grid(row=1, column=0, sticky="w")
#
#     return var
#
# # Функция для выбора файла
# def choose_file():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         file_name_var.set(f".../{file_path.split('/')[-1]}")
#
# # Заглушка для функции продолжения
# def continue_action():
#     pass
#
# # Создаем главное окно приложения
# root = tk.Tk()
# root['bg'] = '#96CDCD'  # Указываем фоновый цвет
# root.title("CSVLoader")
# root.geometry('600x500')  # Указываем размеры окна
#
# # Переменные и поля ввода
# username_var = create_labeled_entry(root, "Username:", 0, 0)
# password_var = create_labeled_entry(root, "Password:", 0, 1, show="*")
# dialect_var = create_labeled_entry(root, "Dialect:", 1, 0)
# database_name_var = create_labeled_entry(root, "Database Name:", 1, 1)
# host_var = create_labeled_entry(root, "Host:", 2, 0, width=70, colspan=2)
#
# # Переменная для отображения имени файла
# file_name_var = tk.StringVar()
#
# # Разделитель
# tk.Frame(root, height=2, bd=1, relief="solid", bg="black").grid(row=3, column=0, columnspan=2, sticky="we", pady=(10, 10))
#
# # Кнопка для выбора файла
# choose_file_button = tk.Button(root, text="Выбрать файл", command=choose_file, width=70)
# choose_file_button.grid(row=4, column=0, padx=15, pady=7, sticky="w", columnspan=2)
#
# # Метка для отображения результата выбора файла
# file_name_label = tk.Label(root, textvariable=file_name_var, width=70, anchor="w", bg=root['bg'])
# file_name_label.grid(row=5, column=0, padx=15, pady=7, sticky="w", columnspan=2)
#
# # Разделитель
# tk.Frame(root, height=2, bd=1, relief="solid", bg="black").grid(row=6, column=0, columnspan=2, sticky="we", pady=(10, 10))
#
# # Кнопка для продолжения
# continue_button = tk.Button(root, text="Продолжить", command=continue_action, width=70)
# continue_button.grid(row=7, column=0, padx=15, pady=7, sticky="w", columnspan=2)
# ----------------------------------------------------------------------------------------------------------------------


# Функция для создания поля с надписью, границей и связанной переменной
def create_labeled_entry(root, label_text, row, column, var, width=20, colspan=1, show=None):
    frame = Frame(root, bd=1, relief="solid", bg=root['bg'])
    frame.grid(row=row, column=column, padx=10, pady=5, sticky="w", columnspan=colspan)

    label = Label(frame, text=label_text, anchor="w", bg=root['bg'])
    label.grid(row=0, column=0, sticky="w")

    entry = Entry(frame, textvariable=var, width=width, show=show)
    entry.grid(row=1, column=0, sticky="w")

def open_convert_window():
    main_window.withdraw()  # Скрываем главное окно
    convert_window.deiconify()  # Показываем окно преобразования

def open_save_db_window():
    main_window.withdraw()  # Скрываем главное окно
    save_db_window.deiconify()  # Показываем окно сохранения

def back_to_main(window):
    window.withdraw()  # Скрываем текущее окно
    main_window.deiconify()  # Показываем главное окно

# Функция для обработки преобразования файла
def handle_convert():
    excel_file = file_name_var.get()
    destination_folder = destination_var.get()
    encoding = encoding_var.get()
    delimiter = delimiter_var.get()

    if excel_file and destination_folder:
        convert_to_csv(excel_file, destination_folder, encoding, delimiter)
    else:
        messagebox.showwarning("Предупреждение", "Выберите файл и папку назначения.")

# ---------------------------------------------------------
# Главное окно приложения
main_window = Tk()
main_window['bg'] = '#96CDCD'
main_window.title("CSVLoader")
main_window.geometry('340x350')
main_window.resizable(width=False, height=False)  # Делаем невозможным менять размеры окна

# Кнопка "Преобразовать файл Excel"
convert_button = Button(main_window, text="Преобразовать файл Excel (xlsx -> csv)", command=open_convert_window,
width=40)
convert_button.pack(pady=40)

# Кнопка "Сохранить файл Excel в базу данных"
save_db_button = Button(main_window, text="Сохранить файл Excel в базу данных", command=open_save_db_window,
 width=40)
save_db_button.pack(pady=20)

# ---------------------------------------------------------
# Окно для преобразования файла Excel в CSV
convert_window = Toplevel(main_window)
convert_window.withdraw()  # Скрываем это окно изначально
convert_window['bg'] = '#96CDCD'
convert_window.title("CSVLoader")
convert_window.geometry('340x350')
convert_window.resizable(width=False, height=False)  # Делаем невозможным менять размеры окна

# Переменные для ввода кодировки и разделителя
encoding_var = StringVar(value="UTF-8")
delimiter_var = StringVar(value=",")

# Рамка для кнопок "Выбрать файл" и "Место назначения"
frame = Frame(convert_window, bd=1, relief="solid", bg=convert_window['bg'])
frame.grid(row=0, column=0, columnspan=2, padx=20, pady=30, sticky="we")

choose_file_button = Button(frame, text="Выбрать файл", command=lambda: file_name_var.set(select_file()))
choose_file_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="w")

choose_destination_button = Button(frame, text="Место назначения", command=lambda: destination_var.set(choose_destination()))
choose_destination_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="w")

# Рамка для
frame_1 = Frame(convert_window, bd=1, relief="solid", bg=convert_window['bg'])
frame_1.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="we")

# Поля для ввода кодировки и разделителя
create_labeled_entry(frame_1, "Кодировка:", 4, 0,  encoding_var)
create_labeled_entry(frame_1, "Разделитель:", 4, 1,  delimiter_var)

# Переменные для хранения выбранного файла и места назначения
file_name_var = StringVar()
destination_var = StringVar()

# Кнопка для преобразования
convert_button = Button(convert_window, text="Преобразовать", command=handle_convert, width=40)
convert_button.grid(row=4, column=0, columnspan=2, padx=20, pady=25)

# Кнопка для возврата в главное окно
back_button = Button(convert_window, text="Назад", command=lambda: back_to_main(convert_window), width=40)
back_button.grid(row=5, column=0, columnspan=2, padx=20, pady=5)

# ---------------------------------------------------------
# Окно для сохранения файла Excel в базу данных (заглушка)
save_db_window = Toplevel(main_window)
save_db_window.withdraw()  # Скрываем это окно изначально
save_db_window['bg'] = '#96CDCD'
save_db_window.title("Сохранение Excel в базу данных")
save_db_window.geometry('400x200')

# Добавьте необходимые элементы и функционал для этого окна аналогично

# Кнопка для возврата в главное окно
back_button = Button(save_db_window, text="Назад", command=lambda: back_to_main(save_db_window), width=40)
back_button.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

# ---------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------
# Запускаем постоянный цикл, чтобы программа работала
# root.mainloop()
# Запуск главного цикла приложения
main_window.mainloop()