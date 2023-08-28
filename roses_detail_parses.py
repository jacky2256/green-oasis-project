from bs4 import BeautifulSoup
import requests
import json



def roses_detail_parser(url_site: str, input_file: str, output_file: str = 'output.json') -> None:
    """
    Function for parsing information about roses.

    Parameters:
    url_site (str): The URL of the site page.
    input_file (str): The link to a text file with links to each rose's page.
    output_file (str, optional): The name of the output JSON file. Defaults to 'output.json'.

    Returns:
    None
    """
    output_url_file = f'output/non_cleaning_data/{output_file}.json'

    with open(input_file, 'r') as file:

        urls = [line.strip() for line in file.readlines()]

        data_list = []
        count = 0


        for url in urls:

            data_dict = {}

            url = url_site + url
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'lxml')

            # Slug Scrapes
            slug = url.split(sep='/')[-1]
            slug = slug.split(sep='.')[0]

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
            data_dict['slug'] = slug
            data_dict['category'] = output_file

            data_list.append(data_dict)

            count += 1
            print(f'#{count}: {url} is done!')

            # Write in the json file

            with open(output_url_file, 'w', encoding='utf-8') as json_file:
                json.dump(data_list, json_file, ensure_ascii=False, indent=4)

            print(f'Data written to {output_url_file}')


    print('Site was scrapping !')
