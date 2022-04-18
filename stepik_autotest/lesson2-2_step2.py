from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elem1 = browser.find_element_by_id('num1')
    elem1 = elem1.text
    elem2 = browser.find_element_by_id('num2')
    elem2 = elem2.text

    click1 = browser.find_element_by_id("dropdown")
    click1.click()

    cul = str(int(elem1) + int(elem2))
    cul1 = int(elem1) + int(elem2)
    print(cul)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(cul)

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()