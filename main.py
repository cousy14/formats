import json
from collections import Counter

with open('newsafr.json', encoding='utf-8') as f:
  data = json.load(f)
# print(data)
  new_list = []
  for item in data['rss']['channel']['items']:
    description_text = item['description'].strip().split(' ')
    for words in description_text:
      if len(words) >= 6:
        new_list.append(words)
  new_dict = Counter(new_list)
  words_top = list(reversed(sorted(new_dict.values())))[:10]      
  for key, value in new_dict.items():
     if value >= words_top[-1]:
      print(value, key)