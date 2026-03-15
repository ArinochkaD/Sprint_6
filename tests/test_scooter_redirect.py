from enum import Enum

import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from tests.order_data import OrderData
from utils.constants import Urls

class TestScooterRedirect:
    driver = None

    @classmethod
    def setup_class(cls):
        driver = webdriver.Firefox()
        cls.driver = driver
        cls.main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        cls.main_page.click_cookies_accept_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.feature('Функциональность редиректа на главную страницу.')
    @allure.description('Проверка редиректа на главную страницу с разных страниц.')
    @pytest.mark.parametrize("is_order_initial", [True, False])
    def test_scooter_logo_redirect(self, is_order_initial):
        main_page = self.main_page
        self.driver.get(Urls.ORDER_URL if is_order_initial else Urls.TRACK_URL)
        main_page.click_scooter_logo()
        main_page.check_base_url(Urls.BASE_URL)
