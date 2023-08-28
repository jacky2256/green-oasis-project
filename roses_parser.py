from roses_url_parser import roses_url_parser
from roses_detail_parses import roses_detail_parser


urls = ['https://kustyroz.ru/catalog/chaino-gibridnie-rozi/',
        'https://kustyroz.ru/catalog/shraby/',
        'https://kustyroz.ru/catalog/anglijskie_rozy/',
        'https://kustyroz.ru/catalog/floribunda-rozi/',
        'https://kustyroz.ru/catalog/pletictie-rozi/',
        'https://kustyroz.ru/catalog/angliyskie_srezochnye_rozy/',
        'https://kustyroz.ru/catalog/kanadskie_rozy/',
        'https://kustyroz.ru/catalog/miniatyurnie-cprei-rozi/',
        'https://kustyroz.ru/catalog/muskusnye_rozy/',
        'https://kustyroz.ru/catalog/pionovidnye_rozy/',
        'https://kustyroz.ru/catalog/poliantovye_rozy/',
        'https://kustyroz.ru/catalog/pochvopokrovnie-rozi/',
        'https://kustyroz.ru/catalog/sadovye_rozy_premium_klassa/',
        'https://kustyroz.ru/catalog/yaponskie_rozy/',
        ]

count_pages = [ 15, 7, 8, 9, 6, 3, 1, 7, 3, 7, 1, 3, 8, 4 ]

for i in range(len(urls)) :
    url = urls[i]
    pages = count_pages[i]

    output_url_file = url.split(sep='/')[-2]
    output_url_file = output_url_file.strip(' ')
    category = output_url_file.replace('-', '_')

    url = f'{url}/?PAGEN_1='

    print(f'scrapping {category} - {url}\n')
    roses_url_parser(count_pages=pages, url_site=url, output_file=f'output/non_cleaning_data/{category}.txt')

    url = 'https://kustyroz.ru'
    roses_detail_parser(url_site=url, input_file=f'output/non_cleaning_data/{category}.txt', output_file=category)

print('\nPROGRAME FINISHED!\n')


