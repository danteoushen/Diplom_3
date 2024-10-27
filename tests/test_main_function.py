from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.order_list_locators import OrdersListLocators
import allure


class TestMainFunction:
    @allure.title('Проверка перехода по клику на кнопку "Конструктор"')
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        main_page.wait_visibility_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        main_page.click_on_constructor_button()
        main_page.wait_visibility_element(MainPageLocators.CREATE_BURGER)
        assert main_page.find_element(MainPageLocators.CREATE_BURGER).text == 'Соберите бургер'

    @allure.title('Проверка перехода по клику на кнопку "Лента заказов"')
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_list()
        main_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        assert main_page.find_element(OrdersListLocators.ORDER_LIST_TITLE).text == 'Лента заказов'

    @allure.title('Проверка появляения всплывающего окна с деталями при клике на ингредиент')
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.find_element(MainPageLocators.INGREDIENTS_DETAILS).is_displayed()

    @allure.title('Проверка закрытия окна с деталями')
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.wait_visibility_element(MainPageLocators.INGREDIENTS_DETAILS)
        main_page.close_details_button()
        main_page.wait_until_element_invisibility(MainPageLocators.INGREDIENTS_DETAILS)
        assert main_page.find_element(MainPageLocators.INGREDIENTS_DETAILS).is_displayed() == False

    @allure.title('Проверка изменения счетчика ингредиента после добавления ингредиента в корзину')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        initial_counter = int(main_page.check_ingredient_counter())
        main_page.add_ingredient_in_order()
        updated_counter = int(main_page.check_ingredient_counter())
        assert updated_counter > initial_counter


    @allure.title('Проверка создания заказа авторизованным пользователем')
    def test_authorized_user_make_order(self, driver,login):
        main_page = MainPage(driver)
        main_page.wait_visibility_element(MainPageLocators.BUN)
        main_page.add_ingredient_in_order()
        main_page.wait_for_element_to_be_clickable(MainPageLocators.MAKE_ORDER_BUTTON)
        main_page.click_make_order()
        main_page.wait_visibility_element(MainPageLocators.ORDER_NUMBER)
        assert main_page.find_element(MainPageLocators.ORDER_ID_TEXT).is_displayed()

