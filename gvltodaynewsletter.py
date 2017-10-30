from lxml import html
from time import sleep
from selenium import webdriver


def parse(url):
    response = webdriver.Chrome()
    response.get(url)
    sleep(3)

    ge1keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[2]/table/tbody/tr/td[2]/div[1]/div')
    print(ge1keyElement.text)
    ge2keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[6]')
    print(ge2keyElement.text)
    ge3keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[7]')
    print(ge3keyElement.text)
    ge4keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[13]')
    print(ge4keyElement.text)
    ge5keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[16]')
    print(ge5keyElement.text)
    ge6keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[17]')
    print(ge6keyElement.text)
    ge7keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[18]')
    print(ge7keyElement.text)
    ge8keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[19]')
    print(ge8keyElement.text)
    ge9keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[20]')
    print(ge9keyElement.text)
    ge10keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[21]')
    print(ge10keyElement.text)
    ge11keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[22]')
    print(ge11keyElement.text)
    ge12keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[23]')
    print(ge12keyElement.text)
    ge13keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[24]')
    print(ge13keyElement.text)
    ge14keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[25]')
    print(ge14keyElement.text)
    ge15keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[26]')
    print(ge15keyElement.text)
    ge16keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[27]')
    print(ge16keyElement.text)
    ge17keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[28]')
    print(ge17keyElement.text)
    ge18keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[39]')
    print(ge18keyElement.text)
    ge19keyElement = response.find_element_by_xpath('//*[@id="archivebody"]/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/div[40]')
    print(ge19keyElement.text)



    sleep(4)



if __name__ == '__main__':

    parse('http://mailchi.mp/gvltoday/hello-greenville-5hwd5cf3t2?e=91100e3012')
