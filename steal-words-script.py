import re
import json
from collections import OrderedDict


content = '****'

words = list()

for find in re.findall('<td.*?>(.+?)</td>', content):
    word = find.split('<')[0].split('&')[0]
    words.append(word)

dictionary = OrderedDict()

for word in range(0, len(words), 5):
    dictionary[words[word]] = {
        'infinitive': words[word+1],
        'past_simple': words[word+2],
        'perfect': words[word+3],
        'russian_translate': words[word+4]
    }


with open('some-words.json', 'w') as f:
    json.dump(dictionary, f, ensure_ascii=False, indent=4)
