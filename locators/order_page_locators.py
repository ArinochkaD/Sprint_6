from selenium.webdriver.common.by import By

class OrderPageLocators:
    """Локаторы страницы Заказа самоката"""
    FIRST_NAME_TEXT_INPUT = [By.XPATH, "//input[@placeholder='* Имя']"]
    LAST_NAME_TEXT_INPUT = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_TEXT_INPUT = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    STATION_TEXT_INPUT = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    PHONE_NUMBER_TEXT_INPUT = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    STATION_ITEMS = [By.XPATH, ".//div[@class='select-search__select']"]
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]
    ORDER_DATE_INPUT = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    ORDER_PERIOD_INPUT = [By.XPATH, "//div[text()='* Срок аренды']"]
    PERIOD_OPTIONS = [By.CSS_SELECTOR, ".Dropdown-option"]
    BLACK_PEARL_COLOR = [By.XPATH, "//label[contains(text(), 'чёрный жемчуг')]"]
    GRAY_HOPELESSNESS_COLOR = [By.XPATH, "//label[text()='серая безысходность']"]
    COMMENT_TEXT_INPUT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"]
    ORDER_DIALOG_SUBMIT = [By.XPATH, "//button[text()='Да']"]
    SUCCESS_ORDER_TITLE = [By.XPATH, "//*[text()='Заказ оформлен']"]

    @staticmethod
    def station_item(index):
        return [By.XPATH, f"//li[@data-index='{index}']"]
