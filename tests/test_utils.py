import os
from unittest.mock import Mock, patch

from src.file_work import WorkingWithJSON
from src.utils import (deleted_option, display_of_number_vacancies, display_of_vacancies, display_range_vacancies,
                       display_top_vacancies)
from tests.test_main import OS_REMOVE_PATH


def test_display_of_vacancies(list_vacancies, capsys):
    display_of_vacancies(list_vacancies)
    captured = capsys.readouterr()
    assert (
        "\n"
        "ID: 120346969\n"
        "Название: Водитель (семейный)\n"
        "Зарплата: 3500000\n"
        "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
        "Хорошо знать город.\n"
        "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
        "\n"
        "ID: 120082289\n"
        "Название: Личный водитель\n"
        "Зарплата: 7500000\n"
        "Требования: Не указаны\n"
        "Ссылка на вакансию: https://hh.ru/vacancy/120082289\n"
    ) == captured.out


def test_display_of_number_vacancies(
    capsys,
    list_vacancies_1,
    list_vacancies_2,
    list_vacancies_5,
    list_vacancies_10,
    list_vacancies_11,
    list_vacancies_21,
    list_vacancies_22,
    list_vacancies_25,
    list_vacancies_100,
):
    display_of_number_vacancies(len(list_vacancies_1), list_vacancies_1)
    captured = capsys.readouterr()
    assert "\nНайдена 1 вакансия, соответствующая вашему запросу\n" == captured.out

    display_of_number_vacancies(len(list_vacancies_2), list_vacancies_2)
    captured = capsys.readouterr()
    assert "\nНайдено 2 вакансии, соответствующие вашему запросу\n" == captured.out

    display_of_number_vacancies(len(list_vacancies_5), list_vacancies_5)
    captured = capsys.readouterr()
    assert "\nНайдено 5 вакансий, соответствующих вашему запросу\n" == captured.out

    display_of_number_vacancies(len(list_vacancies_10), list_vacancies_10)
    captured = capsys.readouterr()
    assert "\nНайдено 10 вакансий, соответствующих вашему запросу\n" == captured.out

    display_of_number_vacancies(len(list_vacancies_11), list_vacancies_11)
    captured = capsys.readouterr()
    assert "\nНайдено 11 вакансий, соответствующих вашему запросу\n" == captured.out

    display_of_number_vacancies(len(list_vacancies_21), list_vacancies_21)
    captured = capsys.readouterr()
    assert "\nНайдена 21 вакансия, соответствующая вашему запросу\n" == captured.out

    display_of_number_vacancies(len(list_vacancies_22), list_vacancies_22)
    captured = capsys.readouterr()
    assert "\nНайдено 22 вакансии, соответствующие вашему запросу\n" == captured.out

    display_of_number_vacancies(len(list_vacancies_25), list_vacancies_25)
    captured = capsys.readouterr()
    assert "\nНайдено 25 вакансий, соответствующих вашему запросу\n" == captured.out

    display_of_number_vacancies(len(list_vacancies_100), list_vacancies_100)
    captured = capsys.readouterr()
    assert "\nНайдено 100 вакансий, соответствующих вашему запросу\n" == captured.out


def test_display_range_vacancies(capsys, list_vacancies_2):
    top_n = 1
    display_range_vacancies(top_n, list_vacancies_2)
    captured = capsys.readouterr()
    assert (
        "\n"
        "ID: 120346969\n"
        "Название: Водитель (семейный)\n"
        "Зарплата: 3500000\n"
        "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
        "Хорошо знать город.\n"
        "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
    ) == captured.out

    top_n = 2
    display_range_vacancies(top_n, list_vacancies_2)
    captured = capsys.readouterr()
    assert (
        "\n"
        "ID: 120346969\n"
        "Название: Водитель (семейный)\n"
        "Зарплата: 3500000\n"
        "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
        "Хорошо знать город.\n"
        "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
        "\n"
        "ID: 120228558\n"
        "Название: Водитель\n"
        "Зарплата: 2250\n"
        "Требования: Опыт работы от 2 лет. Официальное трудоустройство.\n"
        "Ссылка на вакансию: https://hh.ru/vacancy/120228558\n"
    ) == captured.out


def test_deleted_option(capsys, list_vacancies_1, list_vacancies_2):

    for vacancy in list_vacancies_1:
        WorkingWithJSON().add_vacancy(vacancy)
    with patch("builtins.input", Mock(return_value="1")):
        deleted_option(list_vacancies_1)
        captured = capsys.readouterr()
        assert captured.out == "\nВакансия удалена\n"
        assert WorkingWithJSON().get_data_from_file() == []

        os.remove(OS_REMOVE_PATH)

    for vacancy in list_vacancies_2:
        WorkingWithJSON().add_vacancy(vacancy)
    with patch("builtins.input", Mock(return_value="1")):
        deleted_option(list_vacancies_1)
        captured = capsys.readouterr()
        assert captured.out == "\nВакансия удалена\n"
        assert WorkingWithJSON().get_data_from_file() == [
            {
                "id": 120228558,
                "name": "Водитель",
                "salary": 2250,
                "requirement": "Опыт работы от 2 лет. Официальное трудоустройство.",
                "url": "https://hh.ru/vacancy/120228558",
            }
        ]

        os.remove(OS_REMOVE_PATH)

    for vacancy in list_vacancies_2:
        WorkingWithJSON().add_vacancy(vacancy)
    with patch("builtins.input", Mock(return_value="2")):
        deleted_option(list_vacancies_1)
        assert WorkingWithJSON().get_data_from_file() == list_vacancies_2

        os.remove(OS_REMOVE_PATH)

    for vacancy in list_vacancies_1:
        WorkingWithJSON().add_vacancy(vacancy)
    with patch("builtins.input", side_effect=["0", "1"]):
        deleted_option(list_vacancies_1)
        captured = capsys.readouterr()
        assert captured.out == "\nВы ввели неверный номер действия!\n\nВакансия удалена\n"
        assert WorkingWithJSON().get_data_from_file() == []

        os.remove(OS_REMOVE_PATH)

    for vacancy in list_vacancies_2:
        WorkingWithJSON().add_vacancy(vacancy)
    with patch("builtins.input", side_effect=["0", "1"]):
        deleted_option(list_vacancies_1)
        captured = capsys.readouterr()
        assert captured.out == "\nВы ввели неверный номер действия!\n\nВакансия удалена\n"
        assert WorkingWithJSON().get_data_from_file() == [
            {
                "id": 120228558,
                "name": "Водитель",
                "salary": 2250,
                "requirement": "Опыт работы от 2 лет. Официальное трудоустройство.",
                "url": "https://hh.ru/vacancy/120228558",
            }
        ]

        os.remove(OS_REMOVE_PATH)


def test_display_top_no_sorted_vacancies(capsys, list_vacancies_1, list_vacancies_2):

    with patch("builtins.input", Mock(return_value="1")):
        display_top_vacancies(list_vacancies_1)

        captured = capsys.readouterr()
        assert (
            "\n"
            "ID: 120346969\n"
            "Название: Водитель (семейный)\n"
            "Зарплата: 3500000\n"
            "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
            "Хорошо знать город.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
        ) == captured.out

    with patch("builtins.input", side_effect=["2", "2"]):
        display_top_vacancies(list_vacancies_2)
        captured = capsys.readouterr()
        assert (
            "\n"
            "ID: 120346969\n"
            "Название: Водитель (семейный)\n"
            "Зарплата: 3500000\n"
            "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
            "Хорошо знать город.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
            "\n"
            "ID: 120228558\n"
            "Название: Водитель\n"
            "Зарплата: 2250\n"
            "Требования: Опыт работы от 2 лет. Официальное трудоустройство.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120228558\n"
        ) == captured.out

    with patch("builtins.input", side_effect=["2", "1"]):
        display_top_vacancies(list_vacancies_2)
        captured = capsys.readouterr()
        assert (
            "\n"
            "ID: 120228558\n"
            "Название: Водитель\n"
            "Зарплата: 2250\n"
            "Требования: Опыт работы от 2 лет. Официальное трудоустройство.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120228558\n"
            "\n"
            "ID: 120346969\n"
            "Название: Водитель (семейный)\n"
            "Зарплата: 3500000\n"
            "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
            "Хорошо знать город.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
        ) == captured.out

    with patch("builtins.input", side_effect=["0", "1"]):
        display_top_vacancies(list_vacancies_2)
        captured = capsys.readouterr()
        assert (
            "\nНельзя вывести топ 0\n"
            "\n"
            "ID: 120346969\n"
            "Название: Водитель (семейный)\n"
            "Зарплата: 3500000\n"
            "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
            "Хорошо знать город.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
        ) == captured.out

    with patch("builtins.input", side_effect=["0", "2", "1"]):
        display_top_vacancies(list_vacancies_2)
        captured = capsys.readouterr()
        assert (
            "\nНельзя вывести топ 0\n"
            "\n"
            "ID: 120228558\n"
            "Название: Водитель\n"
            "Зарплата: 2250\n"
            "Требования: Опыт работы от 2 лет. Официальное трудоустройство.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120228558\n"
            "\n"
            "ID: 120346969\n"
            "Название: Водитель (семейный)\n"
            "Зарплата: 3500000\n"
            "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
            "Хорошо знать город.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
        ) == captured.out

    with patch("builtins.input", side_effect=["0", "2", "3", "1"]):
        display_top_vacancies(list_vacancies_2)
        captured = capsys.readouterr()
        assert (
            "\n"
            "Нельзя вывести топ 0\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "ID: 120228558\n"
            "Название: Водитель\n"
            "Зарплата: 2250\n"
            "Требования: Опыт работы от 2 лет. Официальное трудоустройство.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120228558\n"
            "\n"
            "ID: 120346969\n"
            "Название: Водитель (семейный)\n"
            "Зарплата: 3500000\n"
            "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
            "Хорошо знать город.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
        ) == captured.out
