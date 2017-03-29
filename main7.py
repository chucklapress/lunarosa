import requests
from bs4 import BeautifulSoup


def communitytapview():

    url = "http://www.thecommunitytap.com/"
    markup = requests.get(url).text
    souper = BeautifulSoup(markup, "lxml")

    looker = souper.find_all(class_='beer')
    for look in looker:
        print(look.text)
    seeker = souper.find_all(class_='wine')
    for seek in seeker:
        print(seek.text)




communitytapview()
