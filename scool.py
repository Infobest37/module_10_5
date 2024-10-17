import os
import datetime

from PIL import Image
# 0:00:05.864658
# Функция которая изменяет размер фотографии
def resize_image(image): # принимает путь к конкретной фотографии
    im = Image.open(image) # Открывает каждую фотографию которую передаем в функцию
    im = im.resize((600, 800)) #  изменяем каждое изображение
    im.save(image) # сохраняем под тем же путем

start = datetime.datetime.now()
for i in range(1, 54):
    image = f"./foto/page_{i}.jpg"
    resize_image(image)
end = datetime.datetime.now()
print(end - start)
# Указываем путь к папке

"""Код для переименования всех файлов"""

# fails = r"C:\Users\user\PycharmProjects\Учеба\10 модуль Потоки\module_10_5\pythonProject\foto"
#
# # Получаем список файлов в папке
# faile = os.listdir(fails)
#
# # Сортируем файлы, чтобы они шли в порядке
# faile.sort()
#
# # Переименовываем файлы
# for index, file_name in enumerate(faile):
#     # Получаем расширение файла
#     file_extension = os.path.splitext(file_name)[1]
#
#     # Формируем новое имя файла (например, 1.txt, 2.txt и т.д.)
#     new_name = f"page_{index + 1}{file_extension}"
#
#     # Полные пути для исходного и нового имени файла
#     old_file = os.path.join(fails, file_name)
#     new_file = os.path.join(fails, new_name)
#
#     # Переименовываем файл
#     os.rename(old_file, new_file)
#
# print("Файлы переименованы!")
