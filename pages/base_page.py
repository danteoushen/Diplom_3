from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def wait_until_element_invisibility(self, locator):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def current_url(self):
        return self.driver.current_url

    def open_site_link(self, url):
        self.driver.get(url)

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    def get_actually_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

