import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_checks_submit_button(browser):
    browser.get(link)
    # time.sleep(20)
    btn = browser.find_elements_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert len(btn) == 1, "There is no submit button on the page"

