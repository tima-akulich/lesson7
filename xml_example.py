import xml.etree.ElementTree as ET

file = open('example.xml', 'r')
tree = ET.parse(file)
root = tree.getroot()
for line in root:
    print(line.text)
file.close()

