import pytest
import requests
from selenium import webdriver
from data import Urls, UserData
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Chrome(options=options)

    browser.get(Urls.URL)
    yield browser
    browser.quit()



@pytest.fixture
def create_and_delete_user():
    payload = UserData.generate_user()
    response = requests.post(Urls.CREATE_USER, data=payload)
    token = response.json()["accessToken"]
    yield response, payload, token
    requests.delete(Urls.DELETE_USER, headers={'Authorization': f'{token}'})

@pytest.fixture
def login(driver,create_and_delete_user):
    page = BasePage(driver)
    page.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    page.wait_visibility_element(PersonalAccountLocators.LOGIN_INPUT_EMAIL)
    email = create_and_delete_user[1]['email']
    password = create_and_delete_user[1]['password']
    page.send_keys(PersonalAccountLocators.LOGIN_INPUT_EMAIL, email)
    page.send_keys(PersonalAccountLocators.LOGIN_INPUT_PASSWORD, password)
    page.click_to_element(PersonalAccountLocators.LOGIN_BUTTON)




