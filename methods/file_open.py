

# from tkinter import StringVar
from tkinter import filedialog


# Функция для выбора файла:
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    return file_path if file_path else None


# Функция для выбора папки места сохранения:
def choose_destination():
    folder_path = filedialog.askdirectory()
    return folder_path if folder_path else None






# Функция для выбора папки места сохранения:
# def choose_destination():
#
#     # Переменная для выбора папки
#     destination_var = StringVar()
#
#     folder_path = filedialog.askdirectory()
#     if folder_path:
#         return destination_var.set(folder_path)


# Функция для выбора файла:
# def select_file():
#
#     # Переменная для выбора файла
#     file_name_var = StringVar()
#
#     file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
#     if file_path:
#         return file_name_var.set(file_path)