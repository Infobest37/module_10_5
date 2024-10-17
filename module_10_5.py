import multiprocessing
from datetime import datetime


def read_info(name):
    all_data =[]
    with open(name, 'r') as f:
        for line in f:
            if not line.strip():  # Проверка на пустую строку
                print('Список в файле окончен')
            all_data.append(line.strip())  # Добавляем строки в список без символов новой строки
    return all_data

# start = datetime.now()
# filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
# for filename in filenames:
#     read_info(filename)
# end = datetime.now()
# print(f"Линейное выполнение заняло: {end - start}")

if __name__ == "__main__":
    start = datetime.now()
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

    # Создание пула с 4 процессами, т.к. у нас 4 файла
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end = datetime.now()
    print(f"Многопроцессное выполнение заняло: {end - start}")
