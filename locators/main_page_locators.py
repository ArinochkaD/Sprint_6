from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы главной страницы"""
    DROPDOWN_BUTTONS = [By.XPATH, ".//div[@class='accordion__button']"]
    TOP_ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Home')]//button[text()='Заказать']"]
    SCOOTER_LOGO_BUTTON = [By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR"]
    YANDEX_LOGO_BUTTON = [By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"]

    @staticmethod
    def dropdown_answer(text, question_number):
        return [By.XPATH, f"//div[@id='accordion__panel-{question_number}']//p[normalize-space(.) = '{text}']"]
