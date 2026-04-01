from src.vacancies import Vacancy


def test_validate_data_and_to_dict():
    assert Vacancy("", "", "", "", "").to_dict() == {
        "id": "Отсутсвует",
        "name": "Отсутствует",
        "salary": 0,
        "requirement": "Не указаны",
        "url": "Ссылка на вакансию отсутствует",
    }

    assert Vacancy(123456789, "", "", "", "").to_dict() == {
        "id": 123456789,
        "name": "Отсутствует",
        "salary": 0,
        "requirement": "Не указаны",
        "url": "Ссылка на вакансию отсутствует",
    }

    assert Vacancy(123456789, "Тестирование", "", "", "").to_dict() == {
        "id": 123456789,
        "name": "Тестирование",
        "salary": 0,
        "requirement": "Не указаны",
        "url": "Ссылка на вакансию отсутствует",
    }

    assert Vacancy(123456789, "Тестирование", 1, "", "").to_dict() == {
        "id": 123456789,
        "name": "Тестирование",
        "salary": 1,
        "requirement": "Не указаны",
        "url": "Ссылка на вакансию отсутствует",
    }

    assert Vacancy(123456789, "Тестирование", 1, "Протестировать класс Vacancy", "").to_dict() == {
        "id": 123456789,
        "name": "Тестирование",
        "salary": 1,
        "requirement": "Протестировать класс Vacancy",
        "url": "Ссылка на вакансию отсутствует",
    }

    assert Vacancy(
        123456789, "Тестирование", 1, "Протестировать класс Vacancy", "https://hh.ru/vacancy/123456789"
    ).to_dict() == {
        "id": 123456789,
        "name": "Тестирование",
        "salary": 1,
        "requirement": "Протестировать класс Vacancy",
        "url": "https://hh.ru/vacancy/123456789",
    }
