from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located(locator))

    def find_elements(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_all_elements_located(locator))

    def find_visible_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.visibility_of_element_located(locator))

    def find_clickable_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.element_to_be_clickable(locator))

    def check_url(self, url):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.url_to_be(url))

    def get_new_window_url(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.until(lambda driver: driver.current_url != "about:blank")
        return self.driver.current_url

    def force_click_element(self, element):
        return self.driver.execute_script("arguments[0].click();", element)
