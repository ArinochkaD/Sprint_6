import pytest
import allure
from selenium import webdriver

from pages.main_page import MainPage
from utils.constants import DropDownAnswers, Urls

class TestDropdownQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        driver = webdriver.Firefox()
        cls.driver = driver
        driver.get(Urls.BASE_URL)
        cls.main_page = MainPage(driver)
        cls.main_page.click_cookies_accept_button()
    
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.feature('Функциональность выпадающего списка в разделе «Вопросы о важном».')
    @allure.description('При нажатии на элемент списка, открывается соответствующий текст.')
    @pytest.mark.parametrize(
        "question_number, answer",
        [
            (0, DropDownAnswers.ANSWER1),
            (1, DropDownAnswers.ANSWER2),
            (2, DropDownAnswers.ANSWER3),
            (3, DropDownAnswers.ANSWER4),
            (4, DropDownAnswers.ANSWER5),
            (5, DropDownAnswers.ANSWER6),
            (6, DropDownAnswers.ANSWER7),
            (7, DropDownAnswers.ANSWER8),
        ]
    )
    def test_open_dropdown_question(self, question_number, answer):
        self.main_page.click_dropdown_question(question_number)
        self.main_page.check_dropdown_answer(answer, question_number)
