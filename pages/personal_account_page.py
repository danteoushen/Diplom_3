from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
import allure


class PersonalAccountPage(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_personal_account_button(self):
        self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_order_history(self):
        self.click_to_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "Выход" ')
    def click_exit(self):
        self.click_to_element(PersonalAccountLocators.EXIT_BUTTON)

    @allure.step('Получить номер заказа в Истории заказов')
    def check_order_number_in_account(self):
        return self.get_actually_text(PersonalAccountLocators.ORDER_NUMBER)

