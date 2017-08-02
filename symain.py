from re import findall,sub
from lxml import html
from time import sleep
from selenium import webdriver
from pprint import pprint
#from xvfbwrapper import Xvfb

def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    otherkeyElement = response.find_element_by_class_name('locu-menu-item-name')
    thekeyElement = response.find_element_by_css_selector('.locu-widget-wrapper #locu-render-output .locu-menu .locu-menu-item .locu-menu-item-name')
    gelkeyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[1]')

    if otherkeyElement:
        otherkeyElement
        print(otherkeyElement.text)
    if thekeyElement:
        thekeyElement
        print(thekeyElement.text)
    if gelkeyElement:
        gelkeyElement
        print(gelkeyElement.text)
        sleep(3)

    parser = html.fromstring(response.page_source,response.current_url)
    gelato = parser.xpath('//*[@id="locu-medium-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]')
    for gelatos in gelato:
        print(gelatos.text)

if __name__ == '__main__':

    parse('http://www.lunarosagelato.com/menu')
