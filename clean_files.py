from data_cleaning.data_cleaning import data_cleaning
import os

folder_path = 'output/non_cleaning_data'  # Замените на путь к вашей папке

input_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

count = 0

for input_file in input_files:

    rose_name = input_file.replace('.json', '')

    input_file = f'output/non_cleaning_data/{input_file}'
    output_file_json = f'output/cleaning_data/{rose_name}.json'
    output_file_csv = f'output/cleaning_data/{rose_name}.csv'

    # print(rose_name, ' - ', input_file, ' - ', output_files_json, ' - ', output_files_csv)

    data_cleaning(input_file=input_file, output_file_json=output_file_json, output_file_csv=output_file_csv)
    count += 1
    print(f'#{count} {input_file} cleaned')

print('PROGRAME FINISHED!')
