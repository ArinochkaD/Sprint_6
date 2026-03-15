import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from tests.order_data import OrderData
from utils.constants import Urls

class TestDzenRedirect:
    driver = None

    @classmethod
    def setup_method(cls):
        driver = webdriver.Firefox()
        cls.driver = driver
        cls.main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        cls.main_page.click_cookies_accept_button()

    @classmethod
    def teardown_method(cls):
        cls.driver.quit()

    @allure.feature('Функциональность открытия новой вкладки dzen.')
    @allure.description('Проверка открытия новой вкладки dzen с разных страниц.')
    @pytest.mark.parametrize("is_order_initial", [True, False])
    def test_yandex_logo_redirect(self, is_order_initial):
        main_page = self.main_page
        self.driver.get(Urls.ORDER_URL if is_order_initial else Urls.TRACK_URL)
        main_page.click_yandex_logo()
        main_page.check_new_window(Urls.DZEN_REDIRECT)
