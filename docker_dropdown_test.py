from selenium import webdriver
import os
import locale
os.environ["PYTHONIOENCODING"] = "utf-8"
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_US.UTF-8")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=chrome_options)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

wait = WebDriverWait(driver,40)

driver.get("https://www.premierleague.com/stats/top/players/total_scoring_att")


cookie_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btn-primary.cookies-notice-accept")))
ActionChains(driver).move_to_element(cookie_button)
driver.execute_script('arguments[0].click();', cookie_button)
wait.until(EC.visibility_of_element_located((By.ID, 'dd-FOOTBALL_COMPSEASON')))

time.sleep(5)
drop_down_click = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.current[data-dropdown-current='FOOTBALL_COMPSEASON']")))
drop_down_click.click()

options = driver.find_elements_by_css_selector("ul[data-dropdown-list='FOOTBALL_COMPSEASON'] li")

for option in options:
  if "2017/18" in option.text.strip():
    option.click()
    time.sleep(6)
    print('That was fun!')

# close driver
driver.close()
