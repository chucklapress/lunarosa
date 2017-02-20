from lxml import html
from time import sleep
from selenium import webdriver


def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    sleep(3)

    ge1keyElement = response.find_element_by_xpath('//*[@id="shopcontent"]/table/tbody/tr/td/table[3]/tbody/tr[2]/td/table/tbody')
    print(ge1keyElement.text)


    sleep(4)


if __name__ == '__main__':

    parse('http://scandpipes.com/group.asp?group=166')
