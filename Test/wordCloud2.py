"""
8. wordfreqcloud2:
Make the word cloud in such a way that when
you hover over each word the frequency is
displayed as a tool tip

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
    print('  ' * indent + '<html>\n<body>\n')
    for k, v in dictObj.items():
        print(' ' * indent, '<font size="', v * 5, '"><abbr title="', v, '">', k, '</abbr></font>')
    print('  ' * indent + '\n</body>\n</html>')


printItems(cnt, 0)
