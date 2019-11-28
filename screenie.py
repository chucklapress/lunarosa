from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.medium.com/')
driver.save_screenshot('screenie.png')
driver.quit()
