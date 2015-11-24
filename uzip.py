"""
The urllib module provides methods for manipulating URLs and downloading
information from the web. The following example downloads and prints
a secret message from
thinkpython.com:
"""
import urllib

zipcode = '02492'

url = 'http://uszip.com/zip/' + zipcode
conn = urllib.urlopen(url)

for line in conn.fp:
    line = line.strip()
    if 'Population' in line:
        print(line)
    if 'Longitude' in line:
        print(line)
    if 'Latitude' in line:
        print(line)

conn.close()
