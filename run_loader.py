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



# https://github.com/ArtemXYZ/csv_loader.git

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
    # convert_window.deiconify()  # Показываем окно преобразования

def open_save_db_window():
    main_window.withdraw()  # Скрываем главное окно
    # save_db_window.deiconify()  # Показываем окно сохранения

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




# ---------------------------------------------------------


# Переменные для ввода кодировки и разделителя
encoding_var = StringVar(value="UTF-8")
delimiter_var = StringVar(value=",")

# Рамка для кнопок "Выбрать файл" и "Место назначения"
frame = Frame(main_window, bd=1, relief="solid", bg=main_window['bg'])
frame.grid(row=0, column=0, columnspan=2, padx=20, pady=30, sticky="we")

choose_file_button = Button(frame, text="Выбрать файл", command=lambda: file_name_var.set(select_file()))
choose_file_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="w")

choose_destination_button = Button(frame, text="Место назначения", command=lambda: destination_var.set(choose_destination()))
choose_destination_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="w")

# Рамка для
frame_1 = Frame(main_window, bd=1, relief="solid", bg=main_window['bg'])
frame_1.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="we")

# Поля для ввода кодировки и разделителя
create_labeled_entry(frame_1, "Кодировка:", 4, 0,  encoding_var)
create_labeled_entry(frame_1, "Разделитель:", 4, 1,  delimiter_var)

# Переменные для хранения выбранного файла и места назначения
file_name_var = StringVar()
destination_var = StringVar()

# Кнопка для преобразования
convert_button = Button(main_window, text="Преобразовать", command=handle_convert, width=40)
convert_button.grid(row=4, column=0, columnspan=2, padx=20, pady=25)

# Кнопка для возврата в главное окно
back_button = Button(main_window, text="Назад", command=lambda: back_to_main(main_window), width=40)
back_button.grid(row=5, column=0, columnspan=2, padx=20, pady=5)
# ---------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------
# Запускаем постоянный цикл, чтобы программа работала
# root.mainloop()
# Запуск главного цикла приложения
main_window.mainloop()