import csv

csvFile = 'datos.csv'
xmlFile = 'datos.xml'

csvdatos = csv.reader(open(csvFile))
xmldatos = open(xmlFile, 'w')
xmldatos.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmldatos.write('<csv_datos>' + "\n")

rowNum = 0
for row in csvdatos:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        xmldatos.write('<row>' + "\n")
        for i in range(len(tags)):
            xmldatos.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmldatos.write('</row>' + "\n")

    rowNum += 1

xmldatos.write('</csv_datos>' + "\n")
xmldatos.close()
