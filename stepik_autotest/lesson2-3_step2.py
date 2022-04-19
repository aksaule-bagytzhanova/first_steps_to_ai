from selenium import webdriver

browser = webdriver.Chrome()

alert = browser.switch_to.alert
alert.accept()

alert = browser.switch_to.alert
alert_text = alert.text

confirm.dismiss()