from pages.base_page import BasePage
from locators.recovery_password_locators import RecoveryPasswordLocators
import allure


class RecoveryPasswordPage(BasePage):

    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_on_recovery_password(self):
        self.click_to_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step('Ввести емейл')
    def input_email(self):
        self.send_keys(RecoveryPasswordLocators.INPUT_EMAIL, 'Alena_Dorofeeva_13_123@mail.ru')

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.click_to_element(RecoveryPasswordLocators.RECOVERY_BUTTON)

    @allure.step('Нажать на кнопку Показать/скрыть пароль')
    def click_show_or_hide_password(self):
        self.click_to_element(RecoveryPasswordLocators.SHOW_OR_HIDE_PASSWORD)

    @allure.step('Проверка активности поля "Пароль"')
    def password_active(self):
        return self.find_element(RecoveryPasswordLocators.ACTIVE_PASSWORD_INPUT)

    @allure.step('Ввод нового пароля')
    def input_password(self):
        self.send_keys(RecoveryPasswordLocators.INPUT_PASSWORD, '123456')

