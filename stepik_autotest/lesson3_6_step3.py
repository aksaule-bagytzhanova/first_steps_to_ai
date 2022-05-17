import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lnk', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_correct_answer(browser, lnk):
    link = f"https://stepik.org/lesson/{lnk}/step/1"
    browser.implicitly_wait(5)
    browser.get(link)
    answer = math.log(int(time.time()))
    print(str(answer))
    input1 = browser.find_element_by_tag_name("textarea")
    input1.send_keys(str(answer))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    correct = browser.find_element_by_class_name("smart-hints__hint").text
    assert "Correct!" == correct, f"Получен неожиданный результат. Ожидаемый результат 'Correct!', полученный результат '{correct}'"
