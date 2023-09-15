from bs4 import BeautifulSoup
import requests
import os
import json

url_site = 'https://kustyroz.ru'

with open('output/url_images_roses.txt') as file_urls:
    urls_roses = [line.strip() for line in file_urls.readlines()]

    data_list = []
    count = 0

    for url_rose in urls_roses:

        url = url_site + '/catalog/' + url_rose + '.html'

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        content = soup.find('div', class_='bx_slider_scroller_container')
        content = soup.find('div', class_='bx_slide')

        # Находим элемент <ul> с id "bx_117848907_779_slider_list"
        ul = content.find('ul')

        # Находим все <li> элементы внутри <ul>
        li_items = ul.find_all('li')

        # Создаем список для хранения URL изображений
        image_urls = []

        # Проходимся по каждому <li> элементу и извлекаем URL изображения
        for li in li_items:
            span = li.find('span', class_='cnt_item')
            if span and 'style' in span.attrs:
                style = span['style']
                url = style.split('background-image:url(')[1].split(')')[0]
                url = url_site + url.replace("'", "")
                image_urls.append(url)

        # Выводим список URL изображений
        # for index, url in enumerate(image_urls, start=1):
        #     print(f"Изображение {index}: {url}")


        # Папка для сохранения изображений
        folder_categorie, rose_name = url_rose.split('/')
        save_folder = f"output/images/"

        # Проходимся по каждому URL изображения и сохраняем его
        for index, url in enumerate(image_urls, start=1):
            data_dict = {}
            response = requests.get(url)
            if response.status_code == 200:
                # Извлекаем расширение файла из URL
                extension = url.split('.')[-1]
                # Составляем имя файла в формате "rose_name_image_1.jpg", "rose_name_image_2.jpg" и т.д. 
                file_name = f"{rose_name}_image_{index}.{extension}"
                data_dict['image'] = f'image_roses/{file_name}'
                data_dict['rose_id'] = rose_name
                data_list.append(data_dict)
                # Полный путь для сохранения
                file_path = os.path.join(save_folder, file_name)
                # Записываем изображение в файл
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"Изображение {file_name} сохранено.")
            else:
                print(f"Не удалось получить изображение {url}")

# Write in the json file

output_url_file = 'output/url_images_roses.json'
with open(output_url_file, 'w', encoding='utf-8') as json_file:
                json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print(f'Data written to {output_url_file}')