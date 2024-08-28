"""
Модуль преобразования файлов Ексель (xlsx -> csv).
"""

# -------------------------------- Стандартные модули
# import io

# -------------------------------- Сторонние библиотеки
import pandas as pd
from tkinter import messagebox
# -------------------------------- Локальные модули




# Функция для преобразования Excel в CSV
def convert_to_csv(excel_file, destination_folder, encod='utf-8', separator=','):
    try:
        # Загружаем Excel файл
        df = pd.read_excel(excel_file)

        # Определяем путь для сохранения CSV файла
        csv_file = f"{destination_folder}/output.csv"

        # Сохраняем DataFrame как CSV
        df.to_csv(csv_file, encoding=encod, sep=separator, index=False)

        # Показать сообщение об успешном преобразовании
        messagebox.showinfo("Успех", "Преобразование завершено")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")











                                                # *** Импорт CSV ***
# ----------------------------------------------------------------------------------------------------------------------






# Мусор
# ----------------------------------------------------------------------------------------------------------------------
# def convert_to_csv(excel_file, destination_folder, encod='utf-8', separator=',',):
#     try:
#         excel_file = file_name_var.get()
#         destination_folder = destination_var.get()
#         encod = encoding_var.get()
#         separator = delimiter_var.get()
#
#         # Загружаем Excel файл
#         df = pd.read_excel(excel_file)
#
#         # Определяем путь для сохранения CSV файла
#         csv_file = f"{destination_folder}/output.csv"
#
#         # Сохраняем DataFrame как CSV
#         df.to_csv(csv_file, encoding=encod, sep=separator, index=False)
#
#         # Показать сообщение об успешном преобразовании
#         messagebox.showinfo("Успех", "Преобразование завершено")
#     except Exception as e:
#         messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")



# def convert_excel_to_csv(file, separator=',', encod='utf-8'):
#     """
#     Конвертация эесель в CSV.
#     """
#
#     # Читаем Excel файла
#     read_excel_file = pd.read_excel(io.BytesIO(file.read()))
#
#     # Создаем объект StringIO для хранения CSV данных в памяти:
#     output = io.StringIO()
#
#
#     # Преобразуем DataFrame в CSV и записываем в StringIO:
#     read_excel_file.to_csv(output, index=False, sep=separator, encoding=encod)
#
#     # Возвращаем указатель в начало StringIO объекта
#     output.seek(0)
#
#     # Читаем CSV данные из StringIO и конвертируем их обратно в DataFrame
#     df_csv = pd.read_csv(output)
#
#     # # ----------------------------------------------
#     # # Получаем CSV строку из StringIO:
#     # csv_ctr_io = output.getvalue()
#
#     # Закрываем StringIO объект для освобождения ресурсов:
#     output.close()
#
#     # print(f'Файл CSV сохранен в DataFrame!')
#
#     return df_csv



# def get_documents_csv():
#
#
#
#
#     if  in ['application/vnd.ms-excel','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
#
#         # Получаем путь к файлу на сервере:
#
#
#         # Скачивание файла
#         file = await bot.download_file(file_path)
#         # print('Скачали документ') +
#
#
#         # # Преобразовываем документ в CSV:
#         df_csv = convert_excel_to_df_csv(file)
#
#
#
#         # if result is True:
#         #
#         #
#         # else:
#
#
#
#
#     else:
#
#         # del_msg = await bot.send_message(chat_id=tg_id, text=f'Пожалуйста, отправьте файл Excel!')
#
# """
# Основной код загрузчика CSV файлов.
#
#
# 0.
# 1. Открываем excel
# 2. Форматируем в CSV (сохраняем куда-то). Можно ли не сохранять а держать в переменной?
# 3. Импортируем CSV в БД (на выбор методы апдейт или инсерт)
# 4. Удаляем CSV.
# """
