from bs4 import BeautifulSoup
import urllib2
url = urllib2.urlopen("https://www.lunarosagelato.com/menu/")
markup = url.read()
soup = BeautifulSoup(markup,"html.parser")
gelato = soup.select('class')


print(soup.prettify())

print('hello')


from bs4 import BeautifulSoup
import urllib2
url = urllib2.urlopen("https://www.lunarosagelato.com/menu/")
markup = url.read()
soup = BeautifulSoup(markup,"html.parser")
for a in soup.find_all('div'):
    print(a)
