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
fname='python.html'
myfile = open(fname,'r+')
def printItems(dictObj, indent):
    myfile.write('  ' * indent + '<html>\n<body>\n<ul>\n')
    for k, v in dictObj.items():
        myfile.write(' ' * indent, '<li>', k, ':', v, '</li>')
    myfile.write('  ' * indent + '</ul>\n</body>\n</html>')
    myfile.close()


printItems(cnt, 0)

