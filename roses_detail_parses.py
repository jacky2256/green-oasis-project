from bs4 import BeautifulSoup
import requests
import csv, json


url_site = 'https://kustyroz.ru'

with open('roses_url_list.txt', 'r') as file:

    urls = [line.strip() for line in file.readlines()]
    data_list = []
    count = 0


    for url in urls:

        data_dict = {}

        url = url_site + url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        # Title Scrapes
        title = soup.find('div', class_='bx-header-section')
        title = soup.find('h1').text
        title = title.split('(')

        if len(title) > 1 :
            title_ru, title_en = title[:2]
            title_en = title_en[:-1]
        else :
            title_en = ''
            title_ru = title[0]

        # Description
        description_rose = soup.find_all('div', class_='bx_lb')
        if len(description_rose) == 1 :
            description_rose = ''
        else :
            description_rose = description_rose[0].find('div', class_='item_info_section')
            description_rose = description_rose.find('div', class_='bx_item_description').text
            # description_rose = description_rose.split('\n')
            # description_rose = description_rose[2]
            # description_rose = description_rose.replace('\xa0', '')


        # Detail
        detail_rose = soup.find('div', class_='bx_item_container')
        detail_rose = detail_rose.find('div', class_='bx_rt')
        detail_rose = detail_rose.find('div', class_='item_info_section')
        dl_element = soup.find('dl')

        dt_elements = dl_element.find_all('dt')
        dd_elements = dl_element.find_all('dd')

        for dt, dd in zip(dt_elements, dd_elements):
            data_dict[dt.text] = dd.text

        data_dict['Название Русское'] = title_ru
        data_dict['Название Английское'] = title_en
        data_dict['Описание'] = description_rose

        data_list.append(data_dict)

        count += 1
        print(f'#{count}: {url} is done!')

        # Write in the csv file

        json_filename = 'output.json'

        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, ensure_ascii=False, indent=4)

        print(f'Data written to {json_filename}')
        #

print('Site was scrapping !')
