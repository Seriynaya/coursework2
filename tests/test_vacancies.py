import json

from src.vacancies import Vacancy
from tests.conftest import city, salary_rate

with open("data/vacancies.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def test_filter_city(city):
    """Тестирование метода фильтрации по городу в классе HH()"""
    test_vac = Vacancy("Костюмер", "Екатеринбург", 22300, data)

    assert test_vac.filter_city() == city


def test_salary_rate(salary_rate):
    """Тестирование метода фильтрации по заработной плате в классе HH()"""
    test_vac = Vacancy("Костюмер", "Екатеринбург", 22300, data)

    city_test = test_vac.filter_city()
    other = test_vac.__le__(0, city_test)
    assert other == salary_rate
