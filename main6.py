import requests
from bs4 import BeautifulSoup






def gelato_scraping_view():

    url = "http://www.lunarosagelato.com"
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    #gelato = souper.find_all('div')
    #for gelato in gelato:
        #print(gelato)
    #finda = souper.find_all('div', attrs={'class':'content page-content'})
    #for find in finda:
        #print(find)
    #seeker = souper.find_all('div', attrs={'class': 'sqs-block-content'})
    #for seek in seeker:
        #print(seek)
    #finder = souper.find_all(class_='sqs-block-content', attrs={'class': 'content id=menu-page'})
    #for find in finder:
        #print(find)
    looker = souper.find_all(class_='sqs-layout sqs-grid-12 columns-12')
    for look in looker:
        print(look)





testing = 1
print(testing)
gelato_scraping_view()
