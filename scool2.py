import datetime
import multiprocessing
from PIL import Image
# 0:00:05.864658
# Функция которая изменяет размер фотографии
def resize_image(image): # принимает путь к конкретной фотографии
    im = Image.open(image) # Открывает каждую фотографию которую передаем в функцию
    im = im.resize((600, 800)) #  изменяем каждое изображение
    im.save(image) # сохраняем под тем же путем


if __name__ == "__main__": # проверка что файл который запускается основной
    with multiprocessing.Pool(processes= 3) as pool: # pool принимает количество процесов сколько нужно запустить
        all_page = []
        for page in range(1, 54):
            all_page.append(f"./foto/page_{page}.jpg")
        start = datetime.datetime.now()
        pool.map(resize_image, all_page)
    end = datetime.datetime.now()
    print(end - start)