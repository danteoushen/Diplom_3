from pages.personal_account_page import PersonalAccountPage
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from data import Urls
import allure



class TestPersonalAccount:
    @allure.title('Проверка перехода на страницу личного кабинета')
    def test_transfer_to_personal_acc(self, driver, login):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_visibility_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_page.click_personal_account_button()
        personal_account_page.wait_visibility_element(PersonalAccountLocators.PROFILE_HEADER)
        new_page = personal_account_page.current_url()
        assert new_page == (Urls.PERSONAL_ACCOUNT)

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_transfer_to_order_list(self, driver, login):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_visibility_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_page.click_personal_account_button()
        personal_account_page.wait_visibility_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        personal_account_page.click_order_history()
        new_page = personal_account_page.current_url()
        assert new_page == (Urls.ORDER_LIST)

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_user(self, driver, login):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_visibility_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_page.click_personal_account_button()
        personal_account_page.wait_visibility_element(PersonalAccountLocators.EXIT_BUTTON)
        personal_account_page.click_exit()
        personal_account_page.wait_visibility_element(PersonalAccountLocators.LOGIN_BUTTON)
        assert personal_account_page.find_element(PersonalAccountLocators.LOGIN_BUTTON).text == 'Войти'

