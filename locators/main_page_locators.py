from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопка "Личный Кабинет" в хэдере
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    # Кнопка "Лента Заказов" в хэдере
    ORDER_LIST_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')
    # Кнопка "Конструктор" в хэдере
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')

    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_ON_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    # Заголовок "Соберите бургер"
    CREATE_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')
    # Ингредиент "Булка"
    BUN = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    # Детали ингредиента
    INGREDIENTS_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    # Закрыть окно с деталями ингредиента
    CLOSE_INGREDIENTS_DETAILS = (By.XPATH, '//div[contains(@class, "pl-10")]/following::button[@type="button"]')
    # Счетчик у ингредиента
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')
    # Корзина
    ORDER_BASKET = By.XPATH, '//ul[contains(@class,"basket")]'
    # Кнопка "Оформить заказ"
    MAKE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    # Идентификатор заказа
    ORDER_ID_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')
    # Номер заказа во всплывающем окне
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "type_digits-large")]'
    # Дефолтный номер заказа во всплывающем окне
    DEFAULT_ORDER = By.XPATH, '//h2[text()="9999"]'
    # Перекрывающий элемент
    COVER_ELEMENT = (By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]"
                               "/following::div[@class='Modal_modal_overlay__x2ZCr']")


