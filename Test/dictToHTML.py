"""
6. wordtags:
Convert the word frequency table into an html document
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


def printItems(dictObj, indent):
    print('  ' * indent + '<html>\n<body>\n<ul>\n')
    for k, v in dictObj.items():
        if isinstance(v, dict):
            print('  ' * indent, '<li>', k, ':', '</li>')
            printItems(v, indent + 1)
        else:
            print(' ' * indent, '<li>', k, ':', v, '</li>')
    print('  ' * indent + '</ul>\n</body>\n</html>')


printItems(cnt, 0)
