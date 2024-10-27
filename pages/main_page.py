from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure



class MainPage(BasePage):

    @allure.step('Переход в Конструктор по клику на кнопку')
    def click_on_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Переход на страницу Лента заказов по клику на кнопку')
    def click_on_order_list(self):
        self.click_to_element(MainPageLocators.ORDER_LIST_BUTTON)

    @allure.step('Кликнуть на ингредиент')
    def click_on_ingredient(self):
        self.click_to_element(MainPageLocators.BUN)

    @allure.step('Закрыть окно c деталями')
    def close_details_button(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENTS_DETAILS)

    @allure.step('Добавить ингредиент в корзину')
    def add_ingredient_in_order(self):
        self.drag_and_drop_on_element(MainPageLocators.BUN, MainPageLocators.ORDER_BASKET)

    @allure.step('Получить количество добавленного в корзину')
    def check_ingredient_counter(self):
        return self.get_actually_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_make_order(self):
        self.click_to_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Закрыть окно заказа')
    def close_order_details(self):
        self.wait_until_element_invisibility(MainPageLocators.COVER_ELEMENT)
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENTS_DETAILS)

