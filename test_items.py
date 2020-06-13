import time
import pytest
from selenium import webdriver


@pytest.fixture()
def language(pytestconfig):
    return pytestconfig.getoption("language")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_add_to_basket_btn_is_displayed(browser, language):
    browser.get(f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')
    time.sleep(30)
    add_to_basket_btn = browser.find_element_by_css_selector("#add_to_basket_form button")
    assert add_to_basket_btn.is_displayed(), 'Кнопка не найдена'
