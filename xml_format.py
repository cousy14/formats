import xml.etree.ElementTree as ET
from collections import Counter

new_list = []
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
news = root.findall('channel/item')
for item in news:
    description_text = item.find('description').text.strip().split(' ')
    for words in description_text:
        if len(words) >= 6:
            new_list.append(words.lower())
new_dict = Counter(new_list)
words_top = list(reversed(sorted(new_dict.values())))[:10]
for key, value in new_dict.items():
 if value >= words_top[-1]:
  print(value, key)           
