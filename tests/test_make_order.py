import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from tests.order_data import OrderData

class TestMakeOrder:
    @allure.feature('Функциональность «Заказать самокат».')
    @allure.description('Проверка полного флоу заказа самоката.')
    @allure.testcase('Вход во флоу заказа от кнопки «Заказать» топ бара.')
    def test_make_order_full_flow_from_top(self, order_data: OrderData, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_page()
        main_page.click_cookies_accept_button()
        main_page.click_order_top_button()
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
        assert order_page.check_success_order()

    @allure.feature('Функциональность «Заказать самокат».')
    @allure.description('Проверка полного флоу заказа самоката.')
    @allure.testcase('Вход во флоу заказа от кнопки «Заказать» из центра страницы.')
    def test_make_order_full_flow_from_home(self, order_data: OrderData, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_page()
        main_page.click_cookies_accept_button()
        main_page.click_order_bottom_button()
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
        assert order_page.check_success_order()
