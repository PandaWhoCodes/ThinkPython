"""
cleanwordfreq:S
Repeat 4 but eliminate noise words
(from noise.txt) from the word frequency table

"""
import re
from collections import Counter

noiseText = []
with open('noise.txt') as noise:
    for lines in noise:
        noiseText = noiseText + lines.split()
Text = []
with open('test.txt') as text:
    for lines in text:
        Text = Text + re.findall(r"[\w']+", lines)
cnt = Counter(Text)
for word, count in cnt.items():
    if word in noiseText:
        cnt[word]=0
        count=0
    if count > 4:
        cnt[word] = 4
for word, count in cnt.items():
    if count!=0:
        print(word + ": " + str(count))
