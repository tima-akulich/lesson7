import json

file = open("news.json", "r")
data = file.read()
file.close()
# загрузка данных из json
data = json.loads(data)
print(data['count'])

# выгрузка в json

data = json.dumps(data)
print(data)

