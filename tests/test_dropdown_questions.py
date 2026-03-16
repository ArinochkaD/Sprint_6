import pytest
import allure

from pages.main_page import MainPage
from utils.constants import DropDownAnswers

class TestDropdownQuestions:
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
    def test_open_dropdown_question(self, question_number, answer, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_cookies_accept_button()
        main_page.click_dropdown_question(question_number)
        assert main_page.check_dropdown_answer(answer, question_number)
