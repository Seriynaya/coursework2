import json

import pytest

from src.vacancies import Vacancy

with open("data/vacancies.json", "r", encoding="utf-8") as file:
    data = json.load(file)


@pytest.fixture
def city():
    """Фикстура для метода фильтрации по городу класса HH()"""
    vacancy = Vacancy("Костюмер", "Екатеринбург", 22300, data)

    return vacancy.filter_city()


@pytest.fixture
def salary_rate():
    """Фикстура для метода фильтрации по заработной плате класса HH()"""
    vacancy = Vacancy("Костюмер", "Екатеринбург", 22300, data)

    city_test = vacancy.filter_city()
    dif = vacancy.__le__(0, city_test)
    return dif
