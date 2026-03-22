import os
from unittest.mock import patch

from src.file_work import WorkingWithJSON
from src.main import user_interaction

OS_REMOVE_PATH = "vacancies.json"

_MOCK_VACANCY_PYTHON_BACKEND = {
    "id": 119780954,
    "name": "Junior Python Backend Developer",
    "salary": 120000,
    "requirement": "Уверенное знание python. Уверенное знание django и DRF. Опыт "
    "работы с git. Опыт работы с PostgreSQL и умение писать SQL...",
    "url": "https://hh.ru/vacancy/119780954",
}


def _mock_get_vacancies(keyword: str, page: int):
    if keyword == "nohtyP":
        return []
    if keyword == "Python-backend":
        return [_MOCK_VACANCY_PYTHON_BACKEND.copy()]
    return []


def test_main_1(capsys):

    with patch("src.main.api_vacancies.get_vacancies", side_effect=_mock_get_vacancies), patch(
        "builtins.input", side_effect=["0", "1", "2", "1", "0", "1", " ", "nohtyP", " ", "test", "0", "101", "1", "6"]
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Вы неверно ввели количество вакансий!\n"
            "\n"
            "Вы неверно ввели количество вакансий!\n"
            "\n"
            "0 вакансий получить нельзя!\n"
            "\n"
            "Больше 100 вакансий получить нельзя!\n"
            "\n"
            "Вакансии по запросу 'nohtyP' не найдены\n"
        )

    with patch("src.main.api_vacancies.get_vacancies", side_effect=_mock_get_vacancies), patch(
        "builtins.input",
        side_effect=["0", "1", "2", "1", "0", "1", " ", "Python-backend", " ", "test", "0", "101", "1", "0", "2", "6"],
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Вы неверно ввели количество вакансий!\n"
            "\n"
            "Вы неверно ввели количество вакансий!\n"
            "\n"
            "0 вакансий получить нельзя!\n"
            "\n"
            "Больше 100 вакансий получить нельзя!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 119780954\n"
            "Название: Junior Python Backend Developer\n"
            "Зарплата: 120000\n"
            "Требования: Уверенное знание python. Уверенное знание django и DRF. Опыт "
            "работы с git. Опыт работы с PostgreSQL и умение писать SQL...\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/119780954\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
        )

    with patch("src.main.api_vacancies.get_vacancies", side_effect=_mock_get_vacancies), patch(
        "builtins.input",
        side_effect=["0", "1", "2", "1", "0", "1", " ", "Python-backend", " ", "test", "0", "101", "1", "0", "1", "6"],
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Вы неверно ввели количество вакансий!\n"
            "\n"
            "Вы неверно ввели количество вакансий!\n"
            "\n"
            "0 вакансий получить нельзя!\n"
            "\n"
            "Больше 100 вакансий получить нельзя!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 119780954\n"
            "Название: Junior Python Backend Developer\n"
            "Зарплата: 120000\n"
            "Требования: Уверенное знание python. Уверенное знание django и DRF. Опыт "
            "работы с git. Опыт работы с PostgreSQL и умение писать SQL...\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/119780954\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вакансии сохранены в файл 'vacancies.json'\n"
        )

        assert WorkingWithJSON().get_data_from_file() == [
            {
                "id": 119780954,
                "name": "Junior Python Backend Developer",
                "requirement": "Уверенное знание python. Уверенное знание django и DRF. Опыт "
                "работы с git. Опыт работы с PostgreSQL и умение писать "
                "SQL...",
                "salary": 120000,
                "url": "https://hh.ru/vacancy/119780954",
            }
        ]
    os.remove(OS_REMOVE_PATH)


def test_main_2_1(capsys, list_vacancies_7, list_vacancies_6_test_1):

    with patch("builtins.input", side_effect=["0", "2", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == "\nВы ввели неверный номер действия!\n\nФайл 'vacancies.json' пуст\n"
        assert WorkingWithJSON().get_data_from_file() is None
        os.remove(OS_REMOVE_PATH)

    for vacancy in list_vacancies_7:
        WorkingWithJSON().add_vacancy(vacancy)

    with patch(
        "builtins.input", side_effect=["0", "2", "3", "2", "0", "1", " ", "abc", "123", "abcabcabc", "123456798", "6"]
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вакансии с ID: '123456798' не найдены\n"
        )

    with patch(
        "builtins.input",
        side_effect=["0", "2", "3", "2", "0", "1", " ", "abc", "123", "abcabcabc", "123456789", "0", "2", "6"],
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 123456789\n"
            "Название: Тест 1\n"
            "Зарплата: 1\n"
            "Требования: Тестирование 1\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/123456789\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
        )

        assert WorkingWithJSON().get_data_from_file() == list_vacancies_7

    with patch(
        "builtins.input",
        side_effect=["0", "2", "3", "2", "0", "1", " ", "abc", "123", "abcabcabc", "123456789", "0", "1", "6"],
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 123456789\n"
            "Название: Тест 1\n"
            "Зарплата: 1\n"
            "Требования: Тестирование 1\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/123456789\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вакансия удалена\n"
        )

        assert WorkingWithJSON().get_data_from_file() == list_vacancies_6_test_1
        os.remove(OS_REMOVE_PATH)


def test_main_2_2(
    capsys,
    list_vacancies_7,
    list_vacancies_6_test_1,
    list_vacancies_5_test_2,
    list_vacancies_4_test_3,
    list_vacancies_3_test_4,
    list_vacancies_2_test_5,
    list_vacancies_1_test_6,
):

    for vacancy in list_vacancies_7:
        WorkingWithJSON().add_vacancy(vacancy)

    with patch("builtins.input", side_effect=["0", "2", "3", "2", "0", "2", " ", "1тсеТ", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Вакансии с названием: '1тсеТ' не найдены\n"
        )
        assert WorkingWithJSON().get_data_from_file() == list_vacancies_7

    with patch("builtins.input", side_effect=["0", "2", "3", "2", "0", "2", " ", "Тест 1", "0", "2", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 123456789\n"
            "Название: Тест 1\n"
            "Зарплата: 1\n"
            "Требования: Тестирование 1\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/123456789\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
        )
        assert WorkingWithJSON().get_data_from_file() == list_vacancies_7

    with patch("builtins.input", side_effect=["0", "2", "3", "2", "0", "2", " ", "Тест 1", "0", "1", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 123456789\n"
            "Название: Тест 1\n"
            "Зарплата: 1\n"
            "Требования: Тестирование 1\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/123456789\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вакансия удалена\n"
        )
        assert WorkingWithJSON().get_data_from_file() == list_vacancies_6_test_1

    with patch("builtins.input", side_effect=["0", "2", "3", "2", "0", "2", " ", "Тестирование", "0", "1", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 342156789\n"
            "Название: Тестирование/2\n"
            "Зарплата: 2\n"
            "Требования: Тестирование 2\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/342156789\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вакансия удалена\n"
        )
        assert WorkingWithJSON().get_data_from_file() == list_vacancies_5_test_2

    with patch("builtins.input", side_effect=["0", "2", "3", "2", "0", "2", " ", "Протестируем", "0", "1", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 431256789\n"
            "Название: /Протестируем/3\n"
            "Зарплата: 3\n"
            "Требования: Тестирование 3\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/431256789\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вакансия удалена\n"
        )
        assert WorkingWithJSON().get_data_from_file() == list_vacancies_4_test_3

    with patch("builtins.input", side_effect=["0", "2", "3", "2", "0", "2", " ", "Протестим", "0", "1", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 432198765\n"
            "Название: -Протестим/4\n"
            "Зарплата: 4\n"
            "Требования: Тестирование 4\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/432198765\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вакансия удалена\n"
        )
        assert WorkingWithJSON().get_data_from_file() == list_vacancies_3_test_4

    with patch("builtins.input", side_effect=["0", "2", "3", "2", "0", "2", " ", "Потестируем", "0", "1", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 432189765\n"
            "Название: -Потестируем-5\n"
            "Зарплата: 5\n"
            "Требования: Тестирование 5\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/432189765\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вакансия удалена\n"
        )
        assert WorkingWithJSON().get_data_from_file() == list_vacancies_2_test_5

    with patch("builtins.input", side_effect=["0", "2", "3", "2", "0", "2", " ", "Потестим", "0", "1", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 4321986765\n"
            "Название: (Потестим/6)\n"
            "Зарплата: 6\n"
            "Требования: Тестирование 6\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/4321986765\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вакансия удалена\n"
        )
        assert WorkingWithJSON().get_data_from_file() == list_vacancies_1_test_6

    with patch("builtins.input", side_effect=["0", "2", "3", "2", "0", "2", " ", "Тестим", "0", "1", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы не ввели поисковой запрос!\n"
            "\n"
            "Найдена 1 вакансия, соответствующая вашему запросу\n"
            "\n"
            "ID: 4329186765\n"
            "Название: (Тестим-7)\n"
            "Зарплата: 7\n"
            "Требования: Тестирование 7\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/4329186765\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вакансия удалена\n"
        )
        assert WorkingWithJSON().get_data_from_file() == []
        os.remove(OS_REMOVE_PATH)


def test_main_3(capsys, list_vacancies_5):

    with patch("builtins.input", side_effect=["0", "3", "6"]):
        user_interaction()  # 01    #02
        captured = capsys.readouterr()
        assert captured.out == "\nВы ввели неверный номер действия!\n\nФайл 'vacancies.json' пуст\n"

    for vacancy in list_vacancies_5:
        WorkingWithJSON().add_vacancy(vacancy)

    with patch("builtins.input", side_effect=["0", "3", "2", "3", "0", "1", "3", "1", "0", "2", " ", "0", "1", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Найдено 5 вакансий, соответствующих вашему запросу\n"
            "\n"
            "Вы неверно ввели топ N!\n"
            "\n"
            "Нельзя вывести топ 0\n"
            "\n"
            "ID: 120082289\n"
            "Название: Личный водитель\n"
            "Зарплата: 7500000\n"
            "Требования: Не указаны\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120082289\n"
        )

    with patch(
        "builtins.input", side_effect=["0", "3", "2", "3", "0", "1", "3", "1", "0", "2", " ", "0", "2", "0", "1", "6"]
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Найдено 5 вакансий, соответствующих вашему запросу\n"
            "\n"
            "Вы неверно ввели топ N!\n"
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
            "ID: 120196391\n"
            "Название: Водитель-снабженец\n"
            "Зарплата: 375000\n"
            "Требования: Пунктуальность и ответственность. — Аккуратное вождение и "
            "бережное отношение к автомобилю.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120196391\n"
        )

    with patch(
        "builtins.input", side_effect=["0", "3", "2", "3", "0", "1", "3", "1", "0", "2", " ", "0", "2", "0", "2", "6"]
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Найдено 5 вакансий, соответствующих вашему запросу\n"
            "\n"
            "Вы неверно ввели топ N!\n"
            "\n"
            "Нельзя вывести топ 0\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "ID: 120082289\n"
            "Название: Личный водитель\n"
            "Зарплата: 7500000\n"
            "Требования: Не указаны\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120082289\n"
            "\n"
            "ID: 120346969\n"
            "Название: Водитель (семейный)\n"
            "Зарплата: 3500000\n"
            "Требования: Опыт работы в семейным водителем. Исполнительность, дисциплина. "
            "Хорошо знать город.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120346969\n"
        )

    with patch(
        "builtins.input",
        side_effect=["0", "3", "2", "3", "0", "1", "3", "1", "0", "1", " ", "abc", "0", " ", "abc", "1", "6"],
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Вы неверно ввели диапазон зарплат!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Вы неверно ввели диапазон зарплат!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Вы неверно ввели диапазон зарплат!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Вы неверно ввели диапазон зарплат!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Найдено 0 вакансий, соответствующих вашему запросу\n"
        )

    with patch(
        "builtins.input",
        side_effect=[
            "0",
            "3",
            "2",
            "3",
            "0",
            "1",
            "3",
            "1",
            "0",
            "1",
            " ",
            "abc",
            "2250",
            " ",
            "abc",
            "375000",
            " ",
            "abc",
            "0",
            "5",
            "0",
            "2",
            "6",
        ],
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Вы неверно ввели диапазон зарплат!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Вы неверно ввели диапазон зарплат!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Вы неверно ввели диапазон зарплат!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Вы неверно ввели диапазон зарплат!\n"
            "\n"
            "Введите диапазон зарплат(От: '2250' - До: '7500000'):\n"
            "\n"
            "Найдено 2 вакансии, соответствующие вашему запросу\n"
            "\n"
            "Вы неверно ввели топ N!\n"
            "\n"
            "Вы неверно ввели топ N!\n"
            "\n"
            "Нельзя вывести топ 0\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "ID: 120196391\n"
            "Название: Водитель-снабженец\n"
            "Зарплата: 375000\n"
            "Требования: Пунктуальность и ответственность. — Аккуратное вождение и "
            "бережное отношение к автомобилю.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120196391\n"
            "\n"
            "ID: 120228558\n"
            "Название: Водитель\n"
            "Зарплата: 2250\n"
            "Требования: Опыт работы от 2 лет. Официальное трудоустройство.\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/120228558\n"
        )
        os.remove('vacancies.json')

def test_main_4(capsys):

    assert WorkingWithJSON().get_data_from_file() is None

    with patch(
        "builtins.input",
        side_effect=[
            "0",
            "4",
            "2",
            "4",
            "0",
            "1",
            " ",
            "abc",
            "123",
            "abcabcabc",
            "123456789",
            "",
            " ",
            "abc",
            "1",
            "",
            "6",
        ],
    ):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == (
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы ввели неверный номер действия!\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "\n"
            "Вы неверно ввели ID!\n"
            "ID состоит из 9 цифр\n"
            "Неверно введена зарплата!\n"
            "Неверно введена зарплата!\n"
            "\n"
            "Вакансия:\n"
            "\n"
            "ID: 123456789\n"
            "Название: Отсутствует\n"
            "Зарплата: 1\n"
            "Требования: Не указаны\n"
            "Ссылка на вакансию: https://hh.ru/vacancy/123456789\n"
            "\n"
            "Записана в файл 'vacancies.json'\n"
        )

        assert WorkingWithJSON().get_data_from_file() == [
            {
                "id": 123456789,
                "name": "Отсутствует",
                "salary": 1,
                "requirement": "Не указаны",
                "url": "https://hh.ru/vacancy/123456789",
            }
        ]


        os.remove("vacancies.json")


def test_main_5(capsys, list_vacancies_1, list_vacancies_2):

    for vacancy in list_vacancies_1:
        WorkingWithJSON().add_vacancy(vacancy)

    with patch("builtins.input", side_effect=["0", "5", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == "\nВы ввели неверный номер действия!\n\nФайл 'vacancies.json' очищен\n"
        assert WorkingWithJSON().get_data_from_file() is None

    for vacancy in list_vacancies_2:
        WorkingWithJSON().add_vacancy(vacancy)

    with patch("builtins.input", side_effect=["0", "5", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == "\nВы ввели неверный номер действия!\n\nФайл 'vacancies.json' очищен\n"
        assert WorkingWithJSON().get_data_from_file() is None

        os.remove(OS_REMOVE_PATH)


def test_main_6(capsys):

    with patch("builtins.input", side_effect=["0", "6"]):
        user_interaction()
        captured = capsys.readouterr()
        assert captured.out == "\nВы ввели неверный номер действия!\n"
