from lxml import html
from time import sleep
from selenium import webdriver


def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    sleep(3)
    #//*[@id="locu-medium-container"]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[1]
    #//*[@id="locu-medium-container"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]
    #grabmenu = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/ul/li[2]').click();

    ge23keyElement = response.find_element_by_xpath('//*[@id="ab2e38de-689d-4b8b-a892-835eb7ea6651"]/div/div/section/div/div[2]/div/div/p')
    print(ge23keyElement.text)
    sleep(2)


if __name__ == '__main__':

    parse('https://lunarosagelato.com/gelateria')
