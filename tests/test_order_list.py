from pages.order_list_page import OrderList
from locators.order_list_locators import OrdersListLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
import allure


class TestOrderList:

    @allure.title('Проверка открытия всплывающего окна с деталями о заказе')
    def test_open_order_details(self, driver):
        list_page = OrderList(driver)
        list_page.click_to_element(MainPageLocators.ORDER_LIST_BUTTON)
        list_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        list_page.check_order_details()
        list_page.wait_visibility_element(OrdersListLocators.ORDER_DETAILS)
        assert list_page.find_element(OrdersListLocators.ORDER_DETAILS).is_displayed()


    @allure.title('Проверка видимости заказа из раздела «История заказов» на странице «Лента заказов»')
    def test_order_visibility_in_history_and_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.wait_visibility_element(MainPageLocators.BUN)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.wait_visibility_element(MainPageLocators.DEFAULT_ORDER)
        main_page.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        main_page.close_order_details()
        acc_page = PersonalAccountPage(driver)
        acc_page.click_personal_account_button()
        acc_page.wait_visibility_element(PersonalAccountLocators.PROFILE_HEADER)
        acc_page.click_order_history()
        acc_page.wait_visibility_element(PersonalAccountLocators.ORDER_NUMBER)
        order = acc_page.check_order_number_in_account()
        main_page.click_on_order_list()
        feed_page = OrderList(driver)
        feed_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        order_in_list = feed_page.find_numbers_order(order)
        assert order in order_in_list

    @allure.title('Проверка увеличения счетчика заказов за все время после создания нового заказа.')
    def test_increase_counter_order_for_all_time(self,driver,login):
        main_page = MainPage(driver)
        list_page = OrderList(driver)
        main_page.click_on_order_list()
        list_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        initial_order_count = list_page.get_total_orders()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_element(MainPageLocators.CREATE_BURGER)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.wait_visibility_element(MainPageLocators.DEFAULT_ORDER)
        main_page.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        main_page.close_order_details()
        main_page.click_on_order_list()
        main_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        updated_order_count = list_page.get_total_orders()
        assert updated_order_count > initial_order_count

    @allure.title('Проверка увеличения счетчика заказов за сегодня после создания нового заказа')
    def test_increase_counter_order_for_today(self, driver, login):
        main_page = MainPage(driver)
        list_page = OrderList(driver)
        main_page.click_on_order_list()
        list_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        initial_order_count = list_page.get_orders_for_today()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_element(MainPageLocators.CREATE_BURGER)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.wait_visibility_element(MainPageLocators.DEFAULT_ORDER)
        main_page.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        main_page.close_order_details()
        main_page.click_on_order_list()
        main_page.wait_visibility_element(OrdersListLocators.ORDER_LIST_TITLE)
        updated_order_count = list_page.get_orders_for_today()
        assert updated_order_count > initial_order_count

    @allure.title('Проверка, что после оформления заказа его номер отображается в разделе "В работе"')
    def test_order_is_in_progress_list(self, driver, login):
        main_page = MainPage(driver)
        list_page = OrderList(driver)
        main_page.wait_visibility_element(MainPageLocators.CREATE_BURGER)
        main_page.add_ingredient_in_order()
        main_page.click_make_order()
        main_page.wait_until_element_invisibility(MainPageLocators.DEFAULT_ORDER)
        main_page.wait_visibility_element(MainPageLocators.ORDER_ID_TEXT)
        order = main_page.get_actually_text(MainPageLocators.ORDER_NUMBER)
        main_page.close_order_details()
        main_page.click_on_order_list()
        orders_in_progress = list_page.check_order_number_in_progress()
        assert order in orders_in_progress

