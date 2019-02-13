# for json
import json

def top_10(items):
    all_words = list()
    count_words = {}
    top = []
    for item in items["rss"]["channel"]["items"]:
        words = item["description"].split()
        for word in words:
            if len(word) > 6:
                all_words.append(word)
        for word in all_words:
            count_words[word] = all_words.count(word)
    number = count_words.values()
    number = sorted(number, reverse=True)
    number = number[9]
    for word, count in count_words.items():
        if count >= number:
            top.append(word)
    # return top # результат больше 10 слов т.к. некоторые слова повторяются
    #одинаковое количество раз
    return top[:10] # для вывода ровно 10 слов

with open("newsafr.json", encoding='utf8') as datafile:
    json_data = json.load(datafile)
    print(top_10(json_data))

# for xml
import xml.etree.ElementTree as ET

def top_10x(items):
    all_words = list()
    count_words = {}
    top = []
    words = items.split()
    for word in words:
        if len(word) > 6:
            all_words.append(word)
    for word in all_words:
        count_words[word] = all_words.count(word)
    number = count_words.values()
    number = sorted(number, reverse=True)
    number = number[9]
    for word, count in count_words.items():
        if count >= number:
            top.append(word)
    return top[:10]

import xml.etree.ElementTree as ET
tree = ET.parse("newsafr.xml")
root = tree.getroot()
xml_root = root.findall("channel/item/description")
xml_list = ''
for news in xml_root:
    xml_list += news.text
print(top_10x(xml_list))
