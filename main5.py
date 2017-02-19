import requests
from bs4 import BeautifulSoup

html = requests.get(
    'http://www.lunarosagelato.com').text
bs = BeautifulSoup(html)
possible_links = bs.find_all('a')
for link in possible_links:
    if link.has_attr('href'):
        print link.attrs['href']
    

from bs4 import BeautifulSoup

bs = BeautifulSoup(html)
for link in bs.find_all('a'):
    if link.has_attr('href'):
        print link.attrs['href']
