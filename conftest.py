import pytest
import sys
import os

from datetime import datetime, timedelta
from selenium import webdriver

from tests.order_data import OrderData

# Добавляем текущую директорию в sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def order_data():
    date = datetime.now() + timedelta(days=1)
    date_order = date.strftime("%d.%m.%Y")
    return OrderData('Арина', 'Тест', 'Улица Пушкина', 1, '71234567890', date_order, 3, 'Нет комментов.')
