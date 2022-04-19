from selenium import webdriver
import time
import math
import os

link = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('aksi')

    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('aksi')

    input3 = browser.find_element_by_name('email')
    input3.send_keys('aksi')

    input4 = browser.find_element_by_id('file')
    input4.send_keys(file_path)

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

