from pages.base_page import BasePage
from locators.order_list_locators import OrdersListLocators
import allure


class OrderList(BasePage):

    @allure.step('Получить детали заказа')
    def check_order_details(self):
        self.click_to_element(OrdersListLocators.ORDER_CARD)

    @allure.step('Получить заказ в Ленте заказов')
    def find_numbers_order(self, order):
        path_to = OrdersListLocators.ORDER_NUMBER_IN_LIST_ORDER[0]
        locator = OrdersListLocators.ORDER_NUMBER_IN_LIST_ORDER[1]
        locator = locator.format(order)
        return self.get_actually_text((path_to, locator))

    @allure.step('Получить заказ в списке заказов в работе')
    def check_order_number_in_progress(self):
        self.wait_visibility_element(OrdersListLocators.READY_ORDERS_TEXT)
        self.wait_until_element_invisibility(OrdersListLocators.READY_ORDERS_TEXT)
        return self.get_actually_text(OrdersListLocators.ORDER_IN_PROGRESS)

    @allure.step('Получить общее количество заказов, выполненных за все время')
    def get_total_orders(self):
        return self.get_actually_text(OrdersListLocators.ALL_TIME_ORDERS)

    @allure.step('Получить общее количество заказов, выполненных за сегодня')
    def get_orders_for_today(self):
        return self.get_actually_text(OrdersListLocators.TODAY_ORDERS)

