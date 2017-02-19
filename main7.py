from lxml import html
import requests
page = requests.get('http://www.lunarosagelato.com/menu')
tree = html.fromstring(page.content)
name = tree.xpath('//*[@id="locu-medium-container"]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[1]/text()')
print(name)
