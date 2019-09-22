from lxml import html
from time import sleep
from selenium import webdriver


def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    iframeElement = response.find_element_by_tag_name('iframe')
    response.switch_to.frame(iframeElement)
    sleep(3)
    ge1keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[1]/div[1]/div[1]')
    ge2keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[2]/div[1]/div[1]')
    ge3keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[3]/div[1]/div[1]')
    ge4keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[4]/div[1]/div[1]')
    ge5keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[5]/div[1]/div[1]')
    ge6keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[6]/div[1]/div[1]')
    ge7keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[7]/div[1]/div[1]')
    ge8keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[8]/div[1]/div[1]')
    ge9keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[9]/div[1]/div[1]')
    ge10keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[10]/div[1]/div[1]')
    ge11keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[11]/div[1]/div[1]')
    ge12keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[12]/div[1]/div[1]')
    ge13keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[13]/div[1]/div[1]')
    ge14keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[14]/div[1]/div[1]')
    ge15keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[15]/div[1]/div[1]')
    ge16keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[16]/div[1]/div[1]')
    ge17keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[17]/div[1]/div[1]')
    ge18keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[18]/div[1]/div[1]')
    ge19keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[19]/div[1]/div[1]')
    ge20keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[20]/div[1]/div[1]')
    ge21keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[21]/div[1]/div[1]')
    ge22keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[22]/div[1]/div[1]')
    ge23keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[23]/div[1]/div[1]')
    #ge24keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[10]/div[24]/div[1]/div[1]')
    #Goofy fix for rouge flavor
    ge24keyElement = response.find_element_by_xpath('//*[@id="locu-medium-container"]/div[1]/div/div/div[4]/div/div[1]/div[1]')

    flavors = open("flavors.txt", "w")

    print(" FLAVORS OF THE DAY ", file=flavors)
    print(" ", file=flavors)
    print(' '+ge1keyElement.text, file=flavors)
    print(' '+ge2keyElement.text, file=flavors)
    print(' '+ge3keyElement.text, file=flavors)
    print(' '+ge4keyElement.text, file=flavors)
    print(' '+ge5keyElement.text, file=flavors)
    print(' '+ge6keyElement.text, file=flavors)
    print(' '+ge7keyElement.text, file=flavors)
    print(' '+ge8keyElement.text, file=flavors)
    print(' '+ge9keyElement.text, file=flavors)
    print(' '+ge10keyElement.text, file=flavors)
    print(' '+ge11keyElement.text, file=flavors)
    print(' '+ge12keyElement.text, file=flavors)
    print(' '+ge13keyElement.text, file=flavors)
    print(' '+ge14keyElement.text, file=flavors)
    print(' '+ge15keyElement.text, file=flavors)
    print(' '+ge16keyElement.text, file=flavors)
    print(' '+ge17keyElement.text, file=flavors)
    print(' '+ge18keyElement.text, file=flavors)
    print(' '+ge19keyElement.text, file=flavors)
    print(' '+ge20keyElement.text, file=flavors)
    print(' '+ge21keyElement.text, file=flavors)
    print(' '+ge22keyElement.text, file=flavors)
    print(' '+ge23keyElement.text, file=flavors)
    print(' '+ge24keyElement.text, file=flavors)

    flavors.close()
    print("It's all good")


if __name__ == '__main__':

    parse('https://lunarosagelato.com/gelateria')
