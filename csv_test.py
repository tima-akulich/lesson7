file = open("example.csv", 'r')

data = file.readlines()
file.close()
headers, data = data[0].split(','), data[1:]

parsed_data = []
for line in data:
    _line = line.split(',')
    _data = {}
    for i, value in enumerate(_line):
        _data[headers[i]] = value
    parsed_data.append(_data)

# print(parsed_data)

headers = ','.join(parsed_data[0].keys())
lines = []
for data in parsed_data:
    lines.append(','.join(data.values()))

file = open('example_copy.txt', 'w')
file.write(headers)
file.writelines(lines)
file.close()

# DICTREADER
import csv

file = open("example.csv", 'r')
reader = csv.DictReader(file)

for line in reader:
    print(line['FIRST NAME '], line['PASSPORT'])

file.close()


# DICTWRITER
data = [{
    'first_name': 'Tima',
    'last_name': 'Akulich'
}]
file = open('example_copy_copy.txt', 'w')
writer = csv.DictWriter(file, ('last_name',))
writer.writeheader()
writer.writerows(data)
file.close()



