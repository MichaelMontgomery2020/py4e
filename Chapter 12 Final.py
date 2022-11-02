import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter count: '))
position = int(input('Enter position: '))

position = position - 1
count = count + 1

# casting tags into list for indexing
while True:

    weblink_database = []

    tags = soup('a')
    for tag in tags:
        # print(tag.get('href',None)) < --- standard tag from py4e example
        weblink_database.append(tag.get('href',None)) # <--- cleaning all tags before placing into list

    nextpage = weblink_database[position]
    nextpage = str(nextpage)
    html = urllib.request.urlopen(nextpage, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = count - 1
    if count == 0:
        break
    # print('count no:',count,'position:',position,nextpage)
    print('Retrieving:',nextpage)
