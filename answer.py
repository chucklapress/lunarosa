from lxml import html
from time import sleep
from selenium import webdriver


def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    #iframeElement = response.find_element_by_tag_name('iframe')
    #response.switch_to.frame(iframeElement)
    sleep(3)

    ge1keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/span/h4')
    ge2keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/span/h4')
    ge3keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[3]/div/div/div[2]/span/h4')
    ge4keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/span/h4')
    ge5keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[5]/div/div/div[2]/span/h4')
    ge6keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[6]/div/div/div[2]/span/h4')
    ge7keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[7]/div/div/div[2]/span/h4')
    ge8keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[8]/div/div/div[2]/span/h4')
    ge9keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[9]/div/div/div[2]/span/h4')
    ge10keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[10]/div/div/div[2]/span/h4')
    ge11keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[11]/div/div/div[2]/span/h4')
    ge12keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[12]/div/div/div[2]/span/h4')
    ge13keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[13]/div/div/div[2]/span/h4')
    #ge14keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[14]/div/div/div[2]/span/h4')
    #ge15keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[15]/div/div/div[2]/span/h4')
    #ge16keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[16]/div/div/div[2]/span/h4')
    #ge17keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[17]/div/div/div[2]/span/h4')
    #ge18keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[18]/div/div/div[2]/span/h4')
    #ge19keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[19]/div/div/div[2]/span/h4')
    #ge20keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[20]/div/div/div[2]/span/h4')
    #ge21keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[21]/div/div/div[2]/span/h4')
    #ge22keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[22]/div/div/div[2]/span/h4')
    #ge23keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[23]/div/div/div[2]/span/h4')
    #ge24keyElement = response.find_element_by_xpath('//*[@id="8c0fcb77-df11-4ac1-a564-56eb92b131ef"]/div/div/section/div/div[1]/div/div/div/div/div/div[2]/div/div[24]/div/div/div[2]/span/h4')

    flavors = open("flavors.txt", "w")

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
    #print(' '+ge14keyElement.text, file=flavors)
    #print(' '+ge15keyElement.text, file=flavors)
    #print(' '+ge16keyElement.text, file=flavors)
    #print(' '+ge17keyElement.text, file=flavors)
    #print(' '+ge18keyElement.text, file=flavors)
    #print(' '+ge19keyElement.text, file=flavors)
    #print(' '+ge20keyElement.text, file=flavors)
    #print(' '+ge21keyElement.text, file=flavors)
    #print(' '+ge22keyElement.text, file=flavors)
    #print(' '+ge23keyElement.text, file=flavors)
    #print(' '+ge24keyElement.text, file=flavors)


    flavors.close()
    print("It's all good")


if __name__ == '__main__':

    parse('https://lunarosagelato.com/gelato-menu')
