from lxml import html
from time import sleep
from selenium import webdriver


def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    #iframeElement = response.find_element_by_tag_name('iframe')
    #response.switch_to.frame(iframeElement)
    sleep(3)
    ge1keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]')
    ge2keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]')
    ge3keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[3]/div/div/div[2]')
    ge4keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]')
    ge5keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[5]/div/div/div[2]')
    ge6keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[6]/div/div/div[2]')
    ge7keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[7]/div/div/div[2]')
    ge8keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[8]/div/div/div[2]')
    #ge9keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[9]/div/div/div[2]')
    #ge10keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[10]/div/div/div[2]')
    #ge11keyElement = response.find_element_by_xpath('//*[@id="4c18f44a-0386-442e-9774-f3d64afe7b13"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[11]/div/div/div[2]')

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
    #print(' '+ge9keyElement.text, file=flavors)
    #print(' '+ge10keyElement.text, file=flavors)
    #print(' '+ge11keyElement.text, file=flavors)

    flavors.close()
    print("It's all good")


if __name__ == '__main__':

    parse('https://lunarosagelato.com/gelateria')
