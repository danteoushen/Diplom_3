from selenium.webdriver.common.by import By


class OrdersListLocators:

    # Счетчик заказов за все время
    ALL_TIME_ORDERS = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"digits-large")]')
    # Счетчик заказов за сегодня
    TODAY_ORDERS = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"digits-large")]')
    # Текст "Все теущие заказы готовы"
    READY_ORDERS_TEXT = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')
    # Заголовок Лента заказов
    ORDER_LIST_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'
    # Карточка заказа
    ORDER_CARD = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")]')
    # Номер заказа в ленте заказов
    ORDER_NUMBER_IN_LIST_ORDER = By.XPATH, '//p[text()="{}"]'
    # Номер заказа в работе
    ORDER_IN_PROGRESS = (By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')
    # Всплывающее окно деталей заказа
    ORDER_DETAILS = (By.XPATH, '//section[contains(@class,"Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]')

