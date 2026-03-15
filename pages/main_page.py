import allure

from locators.general_locators import GeneralLocators
from locators.main_page_locators import MainPageLocators
from pages.general_page import GeneralPage

class MainPage(GeneralPage):
    @allure.step('Принять куки.')
    def click_cookies_accept_button(self):
        try:
            self.find_element(GeneralLocators.COOKIES_ACCEPT_BUTTON).click()
        except Exception:
            print("Ошибка кнопки куки")
    
    @allure.step('Нажать на кнопку «Заказать» вверху страницы.')
    def click_order_top_button(self):
        return self.find_element(MainPageLocators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку «Заказать» снизу страницы.')
    def click_order_bottom_button(self):
        return self.find_element(MainPageLocators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос из выпадающего списка вопросов.')
    def click_dropdown_question(self, question_number):
        elements = self.find_elements(MainPageLocators.DROPDOWN_BUTTONS)
        element = elements[question_number]
        return self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Проверить наличие ответа на вопрос.')
    def check_dropdown_answer(self, text, question_number):
        assert self.find_visible_element(MainPageLocators.dropdown_answer(text, question_number)).is_displayed()

    @allure.step('Нажали на лого самоката.')
    def click_scooter_logo(self):
        return self.find_clickable_element(MainPageLocators.SCOOTER_LOGO_BUTTON).click()

    @allure.step('Проверка возврата на главную страницу.')
    def check_base_url(self, url):
        assert self.check_url(url)

    @allure.step('Нажали на лого Yandex.')
    def click_yandex_logo(self):
        return self.find_clickable_element(MainPageLocators.YANDEX_LOGO_BUTTON).click()

    @allure.step('Проверка нового окна редиректа.')
    def check_new_window(self, url):
        new_window_url = self.get_new_window_url()
        assert url in new_window_url
