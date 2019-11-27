from lxml import html
from time import sleep
from selenium import webdriver


def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    sleep(3)
    name = response.find_element_by_xpath('//*[@id="grpDescrip_75-606-157"]')
    price = response.find_element_by_xpath(' //*[@id="landingpage-price"]/div/div/ul/li[3]')
    details = response.find_element_by_xpath('//*[@id="synopsis"]/div[4]/div/div[10]/ul')


    print("Phone name: " + name.text)
    print("Phone price: " + price.text)
    print("Phone details: " + details.text)

    sleep(1)


if __name__ == '__main__':

    parse('https://www.newegg.ca/p/N82E16875606157')
