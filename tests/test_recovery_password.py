from data import Urls
from locators.recovery_password_locators import RecoveryPasswordLocators
from locators.main_page_locators import MainPageLocators
from pages.recovery_password_page import RecoveryPasswordPage
import allure

class TestRestorePassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по клику на кнопку «Восстановить пароль»')
    def test_click_restore_link_on_main(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.click_to_element(MainPageLocators.LOGIN_BUTTON_ON_MAIN)
        recovery_password_page.click_on_recovery_password()
        recovery_password_page.wait_visibility_element(RecoveryPasswordLocators.RECOVERY_BUTTON)
        recovery_url = recovery_password_page.current_url()
        assert recovery_url == (Urls.FORGOT_PASSWORD)

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»,')
    def test_fill_email_click_restore(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.open_site_link(Urls.RESTORE_PASS)
        recovery_password_page.wait_visibility_element(RecoveryPasswordLocators.RECOVERY_BUTTON)
        recovery_password_page.input_email()
        recovery_password_page.click_on_recovery_button()
        recovery_password_page.wait_visibility_element(RecoveryPasswordLocators.INPUT_PASSWORD)
        recovery_url = recovery_password_page.current_url()
        assert  recovery_url == (Urls.RESTORE_PASS)

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_click_show_pass_input_active(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.open_site_link(Urls.FORGOT_PASSWORD)
        recovery_password_page.wait_visibility_element(RecoveryPasswordLocators.RECOVERY_BUTTON)
        recovery_password_page.input_email()
        recovery_password_page.click_on_recovery_button()
        recovery_password_page.wait_visibility_element(RecoveryPasswordLocators.INPUT_PASSWORD)
        recovery_password_page.input_password()
        recovery_password_page.click_show_or_hide_password()
        recovery_password_page.wait_visibility_element(RecoveryPasswordLocators.ACTIVE_PASSWORD_INPUT)
        check_element = recovery_password_page.password_active()
        assert check_element.is_displayed()

