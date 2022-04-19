from selenium import webdriver
import time
import math

link = 'http://SunInJuly.github.io/execute_script.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num = browser.find_element_by_id('input_value')
    num = num.text

    a = calc(num)

    input1 = browser.find_element_by_css_selector('input')
    input1.send_keys(a)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    button = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    button1 = browser.find_element_by_xpath('//button[text()="Submit"]')
    button1.click()


finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
