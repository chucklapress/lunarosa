from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.wherethetruck.is')
driver.save_screenshot('screenie.png')
driver.quit()
