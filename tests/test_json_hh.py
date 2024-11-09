import json

from src.json_hh import HHVacancy

test_vacancy = [
    {
        "name": "Руководитель коммерческого отдела производственного предприятия",
        "city": "Нижний тагил",
        "salary": {"from": 180000, "to": 300000},
        "url": "https://api.hh.ru/areas/3",
        "description": "Успешный опыт управления продажами в В2В, предпочтительно сегменты, где целевыми"
                       " клиентами являются производственные предприятия (в идеале -сферы металлообработки...",
    },
    {
        "name": "Логист",
        "city": "Екатеринбург",
        "salary": {"from": 80000, "to": 0},
        "url": "https://api.hh.ru/areas/3",
        "description": "Удлиненные полуприцепы вместимостью 110 м3 (или 40 паллет) с усиленной"
                       " цельнометаллической рамой. Опыт работы менеджером транспортного отдела либо диспетчером...",
    },
]


def test_save_vacancy():
    """Тестирование метода сохранения данных в файл"""
    saved = HHVacancy()
    res = saved.save_vacancy(test_vacancy)
    expect = None
    with open("data/searching_vacancies.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    assert res == expect


def test_delete_vacancy():
    """Тестирование метода удаления из файла данных"""
    deleted = HHVacancy()
    deleted.save_vacancy(test_vacancy)
    result = deleted.delete_vacancy("Екатеринбург")
    with open("data/searching_vacancies.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    assert result == data
