import allure

from locators.general_locators import GeneralLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step('Ввели имя.')
    def enter_first_name(self, name):
        return self.find_element(OrderPageLocators.FIRST_NAME_TEXT_INPUT).send_keys(name)

    @allure.step('Ввели фамилию.')
    def enter_last_name(self, last_name):
        return self.find_element(OrderPageLocators.LAST_NAME_TEXT_INPUT).send_keys(last_name)

    @allure.step('Ввели адрес.')
    def enter_address(self, address):
        return self.find_element(OrderPageLocators.ADDRESS_TEXT_INPUT).send_keys(address)

    @allure.step('Выбрали станцию.')
    def select_station(self, station_index):
        self.find_element(OrderPageLocators.STATION_TEXT_INPUT).click()
        self.find_visible_element(OrderPageLocators.STATION_ITEMS)
        return self.find_clickable_element(OrderPageLocators.station_item(station_index)).click()

    @allure.step('Ввели номер телефона.')
    def enter_phone_number(self, phone_number):
        return self.find_element(OrderPageLocators.PHONE_NUMBER_TEXT_INPUT).send_keys(phone_number)

    @allure.step('Нажали кнопку "Далее".')
    def press_next_button(self):
        return self.find_element(OrderPageLocators.NEXT_BUTTON).click()
    
    @allure.step('Заполнили дату.')
    def enter_date_order(self, date):
        self.find_clickable_element(OrderPageLocators.ORDER_DATE_INPUT).send_keys(date)
        return self.find_element(GeneralLocators.BODY).click()

    @allure.step('Заполнили период заказа.')
    def enter_period_order(self, period_index):
        self.find_element(OrderPageLocators.ORDER_PERIOD_INPUT).click()
        elements = self.find_elements(OrderPageLocators.PERIOD_OPTIONS)
        return elements[period_index].click()

    @allure.step('Заполнили цвет самоката.')
    def select_scooter_color(self, locator):
        return self.find_clickable_element(locator).click()

    @allure.step('Заполнили комментарий.')
    def enter_comment(self, text):
        return self.find_element(OrderPageLocators.COMMENT_TEXT_INPUT).send_keys(text)

    @allure.step('Кликнули на кнопку заказать.')
    def order_button_click(self):
        return self.find_element(OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Кликнули на кнопку "Да" в диалоге подтверждения заказа.')
    def order_dialog_submit(self):
        return self.find_clickable_element(OrderPageLocators.ORDER_DIALOG_SUBMIT).click()

    @allure.step('Проверили успешное оформление заказа.')
    def check_success_order(self):
        return self.find_element(OrderPageLocators.SUCCESS_ORDER_TITLE).is_displayed()
