import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from tests.order_data import OrderData
from utils.constants import Urls

class TestMakeOrder:
    driver = None

    @classmethod
    def setup_method(cls):
        driver = webdriver.Firefox()
        cls.driver = driver
        driver.get(Urls.BASE_URL)
        cls.main_page = MainPage(driver)
        cls.order_page = OrderPage(driver)
        cls.main_page.click_cookies_accept_button()

    @classmethod
    def teardown_method(cls):
        cls.driver.quit()

    @allure.feature('Функциональность «Заказать самокат».')
    @allure.description('Проверка полного флоу заказа самоката.')
    @pytest.mark.parametrize("is_top_order_button", [True, False])
    def test_make_order_full_flow(self, is_top_order_button, order_data: OrderData):
        main_page = self.main_page
        order_page = self.order_page
        main_page.click_order_top_button() if is_top_order_button else main_page.click_order_bottom_button()
        order_page.enter_first_name(order_data.first_name)
        order_page.enter_last_name(order_data.last_name)
        order_page.enter_address(order_data.address)
        order_page.select_station(order_data.station_index)
        order_page.enter_phone_number(order_data.phone_number)
        order_page.press_next_button()
        order_page.enter_date_order(order_data.date_order)
        order_page.enter_period_order(order_data.period_index)
        order_page.select_scooter_color(order_data.scooter_color)
        order_page.enter_comment(order_data.comments)
        order_page.order_button_click()
        order_page.order_dialog_submit()
        order_page.check_success_order()
