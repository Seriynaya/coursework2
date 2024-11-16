from src.api_hh import HH
from src.vacancies import Vacancy
from src.json_hh import HHVacancy
from src.utils import filter_vacancies, top_vacancies


def user_interaction():
    """Функция взаимодействия с клиентом"""
    search_query = input("Введите поисковый запрос: ")
    city_search = input("Введите город для поиска вакансии: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary = int(input("Введите желаемую зарплату: "))
    top_n = input("Введите количество вакансий для вывода в топ N: ")
    hh = HH()
    hh.load_vacancies(search_query)
    vacancy = Vacancy(search_query, city_search, salary,hh.vacancies)
    list_cities = vacancy.filter_city()
    list_salary = vacancy.__le__(salary, list_cities)
    filtered_vacancies = filter_vacancies(list_salary, filter_words)
    sd = HHVacancy()
    sd.save_vacancy(filtered_vacancies)
    results = top_vacancies(top_n, filtered_vacancies)
    deleted_vacancy = input("Убрать какие-нибудь вакансии? 'Да / Нет': ")
    if deleted_vacancy == 'Да':
        deleted_words = input('Введите ключевые слова для удаления вакансий: ')
        sd.delete_vacancy(deleted_words)
    return results



print(user_interaction())