import json

def sortByLength(inputStr):
        return len(inputStr)

def repeat(words):
  new_words = []
  for word in words:
    while words.count(word) > 1:
      words.remove(word)
  return new_words

def top_10(items):
  all_words = list()
  for item in items["rss"]["channel"]["items"]:
    words = item["description"].split()
    for word in words:
      if len(word) < 6:
        words.remove(word)
    all_words.extend(words)
  all_words = sorted(all_words, key=sortByLength)
  all_words.reverse()
  repeat(all_words)
  return all_words[:10]


with open("newsafr.json") as datafile:
    json_data = json.load(datafile)
    print(top_10(json_data))
     
