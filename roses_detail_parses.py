from bs4 import BeautifulSoup
import requests
import re


url_site = 'https://kustyroz.ru'
# with open('roses_url_list.txt', 'r') as file:
#     urls = [line.strip() for line in file.readlines()]

#     for url in urls:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, 'lxml')

#         title = soup.find('div', class_='bx-header-section')
#         title = soup.find('h1').text

url = url_site + '/catalog/chaino-gibridnie-rozi/braydal-piano.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

data_dict = {}

# Title Scrapes
# title = soup.find('div', class_='bx-header-section')
# title = soup.find('h1').text
# title = title.split('(')

# if len(title) > 1 :
#     title_ru, title_en = title[:2]
#     title_en = title_en[:-1]
# else :
#     title_en = ''
#     title_ru = title[0]
# print(title_en, title_ru)

# # Description
# description_rose = soup.find_all('div', class_='bx_lb')
# if len(description_rose) == 1 :
#     description_rose = ''
# else :
#     description_rose = description_rose[0].find('div', class_='item_info_section')
#     description_rose = description_rose.find('div', class_='bx_item_description').text
#     description_rose = description_rose.split('\n')
#     description_rose = description_rose[2]
#     description_rose = description_rose.replace('\xa0', '')

# Detail
detail_rose = soup.find('div', class_='bx_item_container')
detail_rose = detail_rose.find('div', class_='bx_rt')
detail_rose = detail_rose.find('div', class_='item_info_section')
dl_elements = soup.find_all('dl')

for dl_element in dl_elements:
    dt_elements = dl_element.find_all('dt')
    dd_elements = dl_element.find_all('dd')
    
    for dt, dd in zip(dt_elements, dd_elements):
        data_dict[dt.text] = dd.text

# data_dict['Название Русское'] = title_ru
# data_dict['Название Английское'] = title_en
# data_dict['Описание'] = description_rose


print(data_dict)
for key, value in data_dict.items():
        print(key, value)
