from lxml import html
from time import sleep
from selenium import webdriver


def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    sleep(3)

    ge1keyElement = response.find_elements_by_css_selector(".locu-widget-wrapper #locu-render-output .locu-menu .locu-menu-item .locu-menu-item-name")
    for element in ge1keyElement:
        print(element.text)



if __name__ == '__main__':

    parse('http://www.lunarosagelato.com/menu')
