from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

text = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
button = browser.find_element_by_id("book")
button.click()

num = browser.find_element_by_id('input_value')
num = num.text

a = calc(num)

input1 = browser.find_element_by_css_selector('input')
input1.send_keys(a)

button1 = browser.find_element_by_xpath('//button[text()="Submit"]')
button1.click()
