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
    sleep(2)
    ge1keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[1]/div[1]')
    print(ge1keyElement.text)
    ge2keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[2]/div[1]')
    print(ge2keyElement.text)
    ge3keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[3]/div[1]')
    print(ge3keyElement.text)
    ge4keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[4]/div[1]')
    print(ge4keyElement.text)
    ge5keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[5]/div[1]')
    print(ge5keyElement.text)
    ge6keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[6]/div[1]')
    print(ge6keyElement.text)
    ge7keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[7]/div[1]')
    print(ge7keyElement.text)
    ge8keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[8]/div[1]')
    print(ge8keyElement.text)
    ge9keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[9]/div[1]')
    print(ge9keyElement.text)
    ge10keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[10]/div[1]')
    print(ge10keyElement.text)
    ge11keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[11]/div[1]')
    print(ge11keyElement.text)
    ge12keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[12]/div[1]')
    print(ge12keyElement.text)
    ge13keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[13]/div[1]')
    print(ge13keyElement.text)
    ge14keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[14]/div[1]')
    print(ge14keyElement.text)
    ge15keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[15]/div[1]')
    print(ge15keyElement.text)
    ge16keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[16]/div[1]')
    print(ge16keyElement.text)
    ge17keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[17]/div[1]')
    print(ge17keyElement.text)
    ge18keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[18]/div[1]')
    print(ge18keyElement.text)
    ge19keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[19]/div[1]')
    print(ge19keyElement.text)
    ge20keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[20]/div[1]')
    print(ge20keyElement.text)
    ge21keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[3]/div[21]/div[1]')
    print(ge21keyElement.text)

    sleep(4)


if __name__ == '__main__':

    parse('http://www.lunarosagelato.com/menu')
