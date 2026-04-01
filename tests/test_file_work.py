import os

from src.file_work import WorkingWithJSON
from tests.test_main import OS_REMOVE_PATH


def test_add_vacancy_and_get_data_from_file(list_vacancies_2):
    for vacancy in list_vacancies_2:
        WorkingWithJSON().add_vacancy(vacancy)
    assert WorkingWithJSON().get_data_from_file() == [
        {
            "id": 120346969,
            "name": "Водитель (семейный)",
            "requirement": "Опыт работы в семейным водителем. Исполнительность, " "дисциплина. Хорошо знать город.",
            "salary": 3500000,
            "url": "https://hh.ru/vacancy/120346969",
        },
        {
            "id": 120228558,
            "name": "Водитель",
            "requirement": "Опыт работы от 2 лет. Официальное трудоустройство.",
            "salary": 2250,
            "url": "https://hh.ru/vacancy/120228558",
        },
    ]
    os.remove(OS_REMOVE_PATH)

    assert WorkingWithJSON().get_data_from_file() is None
    os.remove(OS_REMOVE_PATH)


def test_file_cleaning(list_vacancies_2):
    for vacancy in list_vacancies_2:
        WorkingWithJSON().add_vacancy(vacancy)

    WorkingWithJSON().file_cleaning()

    assert WorkingWithJSON().get_data_from_file() is None
    os.remove(OS_REMOVE_PATH)


def test_delete_vacancy(list_vacancies_1, list_vacancies_2):
    for vacancy in list_vacancies_1:
        WorkingWithJSON().add_vacancy(vacancy)
    WorkingWithJSON().delete_vacancy(list_vacancies_1)
    assert WorkingWithJSON().get_data_from_file() == []

    os.remove(OS_REMOVE_PATH)

    for vacancy in list_vacancies_2:
        WorkingWithJSON().add_vacancy(vacancy)
    WorkingWithJSON().delete_vacancy(list_vacancies_1)
    assert WorkingWithJSON().get_data_from_file() == [
        {
            "id": 120228558,
            "name": "Водитель",
            "requirement": "Опыт работы от 2 лет. Официальное трудоустройство.",
            "salary": 2250,
            "url": "https://hh.ru/vacancy/120228558",
        }
    ]

    os.remove(OS_REMOVE_PATH)
