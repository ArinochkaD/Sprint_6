import pytest
import allure
from pages.main_page import MainPage
from utils.constants import Urls

class TestScooterRedirect:
    @allure.feature('Функциональность редиректа на главную страницу.')
    @allure.description('Проверка редиректа на главную страницу с разных страниц.')
    @pytest.mark.parametrize("initial_url", [Urls.ORDER_URL, Urls.TRACK_URL])
    def test_scooter_logo_redirect(self, initial_url, driver):
        main_page = MainPage(driver)
        main_page.open_page(initial_url)
        main_page.click_cookies_accept_button()
        main_page.click_scooter_logo()
        assert main_page.check_base_url(Urls.BASE_URL)
