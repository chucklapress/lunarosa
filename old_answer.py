from lxml import html
from time import sleep
from selenium import webdriver


def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    sleep(3)
    ge1keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[1]/div[1]')
    ge2keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[2]/div[1]')
    ge3keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[3]/div[1]')
    ge4keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[4]/div[1]')
    ge5keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[5]/div[1]')
    ge6keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[6]/div[1]')
    ge7keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[7]/div[1]')
    ge8keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[8]/div[1]')
    ge9keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[9]/div[1]')
    ge10keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[10]/div[1]')
    ge11keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[11]/div[1]')
    ge12keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[12]/div[1]')
    ge13keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[13]/div[1]')
    ge14keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[14]/div[1]')
    ge15keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[15]/div[1]')
    ge16keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[16]/div[1]')
    ge17keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[17]/div[1]')
    ge18keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[18]/div[1]')
    ge19keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[19]/div[1]')
    ge20keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[20]/div[1]')
    ge21keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[21]/div[1]')
    ge22keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[22]/div[1]')
    ge23keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[2]/div/div/div[5]/div[23]/div[1]')
    print(ge1keyElement.text)
    print(ge2keyElement.text)
    print(ge3keyElement.text)
    print(ge4keyElement.text)
    print(ge5keyElement.text)
    print(ge6keyElement.text)
    print(ge7keyElement.text)
    print(ge8keyElement.text)
    print(ge9keyElement.text)
    print(ge10keyElement.text)
    print(ge11keyElement.text)
    print(ge12keyElement.text)
    print(ge13keyElement.text)
    print(ge14keyElement.text)
    print(ge15keyElement.text)
    print(ge16keyElement.text)
    print(ge17keyElement.text)
    print(ge18keyElement.text)
    print(ge19keyElement.text)
    print(ge20keyElement.text)
    print(ge21keyElement.text)
    print(ge22keyElement.text)
    print(ge23keyElement.text)

    sleep(2)


if __name__ == '__main__':

    parse('https://locu.com/places/luna-rosa-gelato-cafe-greenville-us-2/')