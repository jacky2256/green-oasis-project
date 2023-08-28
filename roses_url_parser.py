from bs4 import BeautifulSoup
import requests

def roses_url_parser(url_site: str, output_file: str = 'output.txt') -> None:
    """
    Function scrapes URLs of each rose from the website www.rose.com.

    Parameters:
    url_site (str): The URL of the site page.
    output_file (str, optional): The name of the output .txt file. Defaults to 'output.txt'.

    Returns:
    None
    """
# h   ttps://kustyroz.ru/catalog/chaino-gibridnie-rozi/?PAGEN_1=
    rose_link_list = []

    for page in range(1,15):
        url = f'{url_site}{page}'

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')


        roses_links = soup.find('div', class_='bx_catalog_list_home')
        roses_links = roses_links.find_all('div',class_='bx_catalog_item')

        for rose_link in roses_links:
            rose_link = rose_link.find('div', class_='bx_catalog_item_container')
            rose_link = rose_link.find('a')                  
            rose_link = rose_link.get('href')
            rose_link_list.append(rose_link)

        print(f'page number {page} is PARSED ')

    with open(output_file, 'a') as file:
        for line in rose_link_list:
            file.write(f'{line}\n')

