import unittest
from unittest.mock import Mock, patch

from src.api import HeadHunterAPI


@patch("src.api.requests.get")
def test_connect_api(mock_get):
    mock_get.return_value.status_code = 200
    assert HeadHunterAPI()._connect_api().status_code == 200
    mock_get.assert_called_once()


class TestGetVacancies(unittest.TestCase):

    @patch("src.api.requests.get")
    def test_get_vacancies(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "items": [
                {
                    "id": "123456789",
                    "name": "Тест 1",
                    "salary": {"from": 1000, "to": 2000},
                    "snippet": {"requirement": "Первое тестирование функции get_vacancies"},
                    "alternate_url": "https://hh.ru/employer/123456789",
                },
                {
                    "id": "987654321",
                    "name": "Тест 2",
                    "salary": {"from": 5000, "to": None},
                    "snippet": {"requirement": "Второе тестирование функции get_vacancies"},
                    "alternate_url": "https://hh.ru/employer/987654321",
                },
                {
                    "id": "897654321",
                    "name": "Тест 3",
                    "salary": {"from": None, "to": 10000},
                    "snippet": {"requirement": "Третье тестирование функции get_vacancies"},
                    "alternate_url": "https://hh.ru/employer/987654321",
                },
            ]
        }
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        vacancies = api.get_vacancies("Тест", 2)

        self.assertEqual(len(vacancies), 3)

        self.assertEqual(vacancies[0]["id"], 123456789)
        self.assertEqual(vacancies[0]["name"], "Тест 1")
        self.assertEqual(vacancies[0]["salary"], 1500)
        self.assertEqual(vacancies[0]["requirement"], "Первое тестирование функции get_vacancies")
        self.assertEqual(vacancies[0]["url"], "https://hh.ru/employer/123456789")

        self.assertEqual(vacancies[1]["id"], 987654321)
        self.assertEqual(vacancies[1]["name"], "Тест 2")
        self.assertEqual(vacancies[1]["salary"], 5000)
        self.assertEqual(vacancies[1]["requirement"], "Второе тестирование функции get_vacancies")
        self.assertEqual(vacancies[1]["url"], "https://hh.ru/employer/987654321")

        self.assertEqual(vacancies[2]["id"], 897654321)
        self.assertEqual(vacancies[2]["name"], "Тест 3")
        self.assertEqual(vacancies[2]["salary"], 10000)
        self.assertEqual(vacancies[2]["requirement"], "Третье тестирование функции get_vacancies")
        self.assertEqual(vacancies[2]["url"], "https://hh.ru/employer/987654321")
