class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "city", "salary", "result", "data_base_hh")

    def __init__(self, name, city, salary, data_base_hh):
        """Инициализатор для класса"""
        self.name = name
        self.city = city
        self.salary = salary
        self.data_base_hh = data_base_hh
        self.result = []
        self.__reform_file(self.data_base_hh)

    def __reform_file(self, data_hh):
        """Метод для обработки JSON-ответа от сайта HH.ru"""
        for info in data_hh:
            name = info["name"]
            city = info["area"]["name"]
            url = info["alternate_url"]
            description = info["snippet"]["requirement"]

            salary_from = info["salary"]["from"] if info["salary"] and info["salary"]["currency"] == "RUR" else 0
            salary_to = info["salary"]["to"] if info["salary"] and info["salary"]["currency"] == "RUR" else 0

            if info["salary"] is None:
                salary_from, salary_to = 0, 0
            elif info["salary"]["from"] is None:
                salary_from = 0
            elif info["salary"]["to"] is None:
                salary_to = 0

            self.result.append(
                {
                    "name": name,
                    "city": city,
                    "salary": {"from": salary_from, "to": salary_to},
                    "url": url,
                    "description": description,
                }
            )

    def filter_city(self):
        """Метод фильтрации списка вакансий по нужному городу"""
        list_cities = []
        for city in self.result:
            if self.city == city["city"]:
                list_cities.append(city)
        return list_cities

    def __le__(self, other, my_list):
        """Магический метод фильтрации списка вакансий по заработной плате"""
        list_salary = []
        for salary in my_list:
            if other <= salary["salary"]["from"]:
                list_salary.append(salary)
        return list_salary
