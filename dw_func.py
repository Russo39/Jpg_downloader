import urllib.request
import re
import os

def download_image_from_file(filename):
    if not os.path.exists('Images'):
        os.mkdir('Images') 
    with open(filename, 'r') as file:
        uncorrect_ulrs = []
        # Задаём начало отсчёта
        n=1
        # Перебор строк в файле
        for f in file:
            # Удаление пробелов
            dw_file=f.strip()
            # Добавление https:// для корреткного скачивания
            url = 'https://' + dw_file
            # Проверка на корректную ссылку
            pattern = r"\.jpg\S*"
            url = re.sub(pattern, '.jpg', url)
            correct_check = re.search(pattern, url)
            if correct_check:
                try:
                    # Указание пути куда сохранять + название файла
                    pattern_2 = r'\w+.jpg'
                    abcde = re.findall(pattern_2, url)
                    #os.mkir('Images')
                    #image_name = 'C:/Python_projects/Images/' + abcde[0]
                    image_name = 'Images/' + abcde[0]
                    # Скачивание и сохранение файла
                    urllib.request.urlretrieve(url, image_name)
                    print(f'Ссылка {url} обработана')
                except:
                    print(f'Ошибка, файл по ссылке не обработан\n{url}')
                    continue
            else:
                print(f'Ссылка не на картинку!!!!!!!\n{url}')
                uncorrect_ulrs.append(url)
                continue
    print(f'Не обработано {len(uncorrect_ulrs)} ссылок')
    for i in uncorrect_ulrs:
        print(i)