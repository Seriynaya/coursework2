import json
import os.path
from abc import ABC, abstractmethod


class JSONVacancy(ABC):
    """Абстрактный метод создания и удаления JSON-файлов"""

    @abstractmethod
    def save_vacancy(self, stock_list):
        """Метод сохранения вакансий в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, words_del):
        """Метод удаления неподходящей информации"""
        pass


class HHVacancy(JSONVacancy):
    """Класс создания и удаления вакансий HH.ru"""

    def __init__(self, file_name_save="data/searching_vacancies.json"):
        """Инициализатор класса"""
        self.__file_name_save = file_name_save

    def file_name(self):
        return self.__file_name_save

    def save_vacancy(self, data_list):
        """Метод сохранения вакансий в файл"""
        if data_list is not None:
            if os.path.exists(self.file_name()):
                with open(self.file_name(), "r", encoding="utf-8") as file:
                    data = json.load(file)
            else:
                data = []

            # Обновляем список данных, добавляя отсутствующие вакансии
            for info in data_list:
                if info not in data:
                    data.append(info)

            with open(self.file_name(), "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        else:
            print("Таких вакансий не найдено")

    def delete_vacancy(self, delete_words):
        """Метод удаления неподходящей информации"""
        if not os.path.exists(self.file_name()):
            return "Такой информации не найдено"

        with open(self.file_name(), "r", encoding="utf-8") as file:
            data = json.load(file)

        # Фильтруем данные с использованием генератора списков
        new_data = [
            info
            for info in data
            if delete_words != info["city"]
            and delete_words not in info["name"]
            and delete_words not in info["description"]
        ]

        # Сохраняем обновленные данные обратно в файл
        with open(self.file_name(), "w", encoding="utf-8") as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)

        return new_data
