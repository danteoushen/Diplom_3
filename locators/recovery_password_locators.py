from selenium.webdriver.common.by import By


class RecoveryPasswordLocators:

    # Кнопка "Восстановить пароль"
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, '//a[@href = "/forgot-password"]')
    # Ввод почты
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    # Кнопка "Восстановить"
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    # Ввод пароля
    INPUT_PASSWORD = (By.XPATH, '//input[@type="password"]')
    # Кнопка "показать/скрыть пароль"
    SHOW_OR_HIDE_PASSWORD = (By.XPATH, '//div[contains(@class,"icon-action")]')
    # Поле ввода пароля активно
    ACTIVE_PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]')

