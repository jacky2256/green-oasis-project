import pandas


def data_cleaning(input_file: str, output_file_json: str, output_file_csv: str) -> None:

    """
    Function for cleaning .json file.

    Parameters:
    input_file: The path of file that needs to be cleaned.
    output_file_json: A path to save the cleaned data in .json format.
    output_file_csv: A path to save the cleaned data in .csv format.

    Returns:
    Two files: *.json and *.csv
    """

    df_base = pandas.read_json(input_file)
   
    # Высота цветка
    df_base[['min_bush_height', 'max_bush_height', 'unit']] = df_base['Высота куста'].str.extract(r'(\d+)-?(\d*)\s*(?:–|-)?\s?(\d*)\s?(?:см)?')
    
    # Количество цветков на стебле
    df_base[['min_number_flawers', 'max_number_flawers', 'unit']] = df_base['Количество цветков на стебле'].str.extract(r'(\d+)-?(\d*)\s*([^\d\s]*)')

    # Размер цветка
    df_base[['min_size_number', 'max_size_number', 'unit']] = df_base['Размер цветка'].str.extract(r'(\d+)-?(\d*)\s*(?:–|-)?\s?(\d*)\s?(?:см)?')
    
    # Цветение
    # Создаем словарь замен
    replacement_dict = {
        'Повторноцветущая': 'повторноцветущая',
        'Повторноцветущая ': 'повторноцветущая',
        'Повторно цветущая': 'повторноцветущая',
        'повторноцветущая': 'повторноцветущая',
        'Повторное': 'повторноцветущая',
        'Обильное': 'обильное',
        'Обильное ': 'обильное',
        'неоднократное обильное': 'обильное',
        'непрерывноцветущая': 'непрерывноцветущая',
        'Непрерывноцветущая': 'непрерывноцветущая',
        'Непрерывноцветущая ': 'непрерывноцветущая'
    }

    # Применяем замены
    df_base['Цветение'] = df_base['Цветение'].replace(replacement_dict, regex=True)

    # Устойчивость к дождю
    # Создаем словарь замен
    replacement_dict = {
        'Средняя, повреждаются некоторые цветки': 'средняя',
        'Слабая, при дожде цветки не раскрываются ': 'слабая',
        'Слабая': 'слабая',
        'Высокая': 'сильная',
        '++': 'средняя',
        'Очень хорошая, цветки дождем не портятся': 'сильная',
        '+': 'слабая',
        'Средняя': 'средняя',
        'Средняя ': 'средняя',
        'Высокая ': 'сильная',
        '+++ ': 'сильная',
        'Слабая, при дожде цветки не раскрываются': 'слабая',
        'Средняя, повреждаются некоторые цветки ': 'средняя',
        'Слабая, при дожде цветки не раскрываются ': 'слабая',
        'Средняя, повреждаются некоторый цветки': 'средняя',
        '+++': 'сильная',
    }

    # Применяем замены
    df_base['Устойчивость к дождю'] = df_base['Устойчивость к дождю'].replace(replacement_dict)
    # Устойчивость к мучнистой росе
    # Создаем словарь замен
    replacement_dict = {
        'Средняя': 'средняя',
        'Слабая': 'слабая',
        'Слабая': 'слабая',
        'Высокая': 'сильная',
        '++': 'средняя',
        '2': 'средняя',
        '+': 'слабая',
        'Средняя': 'средняя',
        'Средняя ': 'средняя',
        'Высокая ': 'сильная',
        '3': 'сильная',
        '1': 'слабая',
        '+++': 'сильная',
        'Очень хорошая': 'сильная'
    }

    # Применяем замены
    df_base['Устойчивость к мучнистой росе'] = df_base['Устойчивость к мучнистой росе'].replace(replacement_dict)
   
    # Устойчивость к черной пятнистости
    # Создаем словарь замен
    replacement_dict = {
        'Средняя': 'средняя',
        'Слабая': 'слабая',
        'Слабая': 'слабая',
        'Высокая': 'сильная',
        '++': 'средняя',
        '2': 'средняя',
        '+': 'слабая',
        'Средняя': 'средняя',
        'Средняя ': 'средняя',
        'Высокая ': 'сильная',
        '3': 'сильная',
        '1': 'слабая',
        '+++': 'сильная',
        'Очень хорошая': 'сильная'
    }

    # Применяем замены
    df_base['Устойчивость к черной пятнистости'] = df_base['Устойчивость к черной пятнистости'].replace(replacement_dict)

    # USDA
    df_base['USDA'] = df_base['USDA'].str.extract(r'(\d+)')

    # Убираем пробелы
    df_base['Название Английское'] = df_base['Название Английское'].str.strip()
    df_base['Название Русское'] = df_base['Название Русское'].str.strip()
    
    # Описание
    df_finish = df_base.copy()
    df_finish = df_finish.drop(['Высота куста', 'Количество цветков на стебле', 'Размер цветка', 'unit'], axis=1)
  
    column_name_mapping = {
        'Название Английское': 'title_en',
        'Название Русское': 'title_ru',
        'Цвет': 'color',
        'Аромат': 'aroma',
        'Цветение': 'flowering',
        'Устойчивость к дождю': 'rain_resistance',
        'Устойчивость к мучнистой росе': 'powdery_mildew_resistance',
        'Устойчивость к черной пятнистости': 'black_spot_resistance',
        'Описание': 'description',
        'USDA': 'usda',
        'Производитель': 'greenhouse',
    }

    df_finish.rename(columns=column_name_mapping, inplace=True)

    # df_finish['category'] = 'hybrid_tea_rose'
    df_finish['in_stock'] = 'yes'
    
    desired_column_order = [
        'title_en', 'title_ru', 'color', 'aroma', 'max_bush_height', 'min_bush_height',
        'max_number_flawers', 'min_number_flawers', 'max_size_number', 'min_size_number',
        'rain_resistance', 'powdery_mildew_resistance', 'black_spot_resistance', 'description',
        'greenhouse', 'category', 'in_stock', 'slug',
    ]

    df_finish = df_finish[desired_column_order]
    
    df_description = df_finish['description'].copy()
    
    pandas.set_option('display.max_colwidth', None)

    df_description.str.strip(to_strip='\n')
    df_finish['description'] = df_finish['description'].str.replace(r'^\s*Полное описание\n', '', regex=True)

    
    df_finish['description'] = df_finish['description'].str.replace(r'Для отправки заказчику.*', '', regex=True)
    
    df_finish['description'] = df_finish['description'].str.replace(r'Заказать саженцы роз.*', '', regex=True)
   
    df_finish['description'] = df_finish['description'].str.replace(r'^(.*?[А-Яа-я])', r'\1', regex=True)
    
    df_finish['description'] = df_finish['description'].str.replace(r'[\n\r\t]', '', regex=True)
   
    df_finish['description'] = df_finish['description'].str.replace(r'  Заказать.*', '', regex=True)
    
    df_finish.to_json(output_file_json, orient='records')  # orient='records' сохранит данные в виде списка записей

    df_finish.to_csv(output_file_csv, index=False)  # index=False, чтобы не сохранять индексы