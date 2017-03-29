import requests
from bs4 import BeautifulSoup
from pprint import pprint






def communitytapview():

    url = "http://www.thecommunitytap.com/"
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")

    looker = souper.find_all(class_='beer')
    for look in looker:
        pprint(look.text)
    seeker = souper.find_all(class_='wine')
    for seek in seeker:
        pprint(seek.text)




communitytapview()
