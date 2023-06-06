# Read user input
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
numbers = list()
result = 0
for tag in tags:
    # Look at the parts of a tag
    x = str(tag)
    y = re.findall('([0-9]+)', x)
    if len(y) == 0:
        continue
    else:
        for i in y:
            result += int(i)
            numbers.append(i)
print(result)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)

# print(tag.get('href', None))
# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')
#
# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)