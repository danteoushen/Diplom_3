from selenium.webdriver.common.by import By


class PersonalAccountLocators:

    # Кнопка "История заказов"
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    # Ввод почты
    LOGIN_INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    # Ввод пароля
    LOGIN_INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    # Заголовок "Профиль"
    PROFILE_HEADER = (By.XPATH, '//a[text()="Профиль"]')
    # Номер заказа
    ORDER_NUMBER = (By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]')
    # Кнопка ""Выход"
    EXIT_BUTTON = (By.XPATH, '//button[text() = "Выход"]')

