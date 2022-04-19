from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    inp1 = browser.find_element_by_css_selector('button')
    inp1.click()

    first_window = browser.window_handles[1]
    browser.switch_to.window(first_window)

    num = browser.find_element_by_id('input_value')
    num = num.text

    a = calc(num)

    input1 = browser.find_element_by_css_selector('input')
    input1.send_keys(a)

    button1 = browser.find_element_by_xpath('//button[text()="Submit"]')
    button1.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

