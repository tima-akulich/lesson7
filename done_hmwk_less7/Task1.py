import argparse
import csv
import json

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('--file', dest='f', required=True,
                        type=str, help='name of file')
parser.add_argument('--from-format', dest='ff',
                        type=str, help='conversion from format')
parser.add_argument('--to-format', dest='tf',
                        type=str, help='conversion to format')
result = parser.parse_args()

if result.f:
    if result.ff == 'csv':
        file_csv = open("example.csv", 'r')
        reader = csv.DictReader(file_csv)
        if result.tf == "json":
            result_conv = json.dumps(list(reader))
            file_json_res = open('res_of_convert_cvs_to_json', 'w')
            file_json_res.writelines(result_conv)
            file_json_res.close()
        file_csv.close()
    elif result.ff == 'json':
        file_json = open('news.json', 'r')
        data = file_json.read() # почему-то падает
        if result.tf == 'csv':
            file_csv_res = open('res_of_convert_json_to_cvs', 'w')
            fieldnames = ','.join(data[0].keys()) # пытаюсь взять хедеры по ключам в джейсоне
            writer = csv.DictWriter(file_csv_res, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            file_csv_res.close()
        file_json.close()
    else:
        print('wrong!')