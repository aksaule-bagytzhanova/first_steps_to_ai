from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_css_selector("input.second")
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("some@gmail.com")

    input4 = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']")
    input4.send_keys("878787878")

    input5 = browser.find_element_by_xpath("//input[@placeholder='Input your address:']")
    input5.send_keys("Russia")

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла