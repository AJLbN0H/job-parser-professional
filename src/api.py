from abc import ABC, abstractmethod

import requests


class API(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def _connect_api(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, page) -> list:
        pass


class HeadHunterAPI(API):
    """Класс отвечающий за подключение к API hh.ru и получение вакансий по ключевому слову, количеству получаемых вакансий"""


    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"text": "вОДИТЕЛЬ", "per_page": 100}

    def _connect_api(self):
        """Метод подключения к API сайта hh.ru"""

        response = requests.get(self.__url, params=self.__params)
        return response

    def get_vacancies(self, keyword: str, page: int) -> list:
        """Получение вакансий с API сайта hh.ru по ключевому слову и количеству получаемых вакансий"""

        self.__params["text"] = keyword
        self.__params["per_page"] = page
        response = self._connect_api()

        dict_vacancy = []

        if response and response.status_code == 200:
            vacancies = response.json().get("items", [])

            for vacancy in vacancies:
                if vacancy["id"] not in dict_vacancy:
                    if (
                        vacancy["salary"]
                        and vacancy["salary"]["from"] is not None
                        and vacancy["salary"]["to"] is not None
                    ):

                        average_salary = round((vacancy["salary"]["from"] + vacancy["salary"]["to"]) / 2)
                        dict_vacancy.append(
                            {
                                "id": int(vacancy["id"]),
                                "name": vacancy["name"],
                                "salary": average_salary,
                                "requirement": vacancy["snippet"]["requirement"],
                                "url": vacancy["alternate_url"],
                            }
                        )

                    elif vacancy["salary"] and vacancy["salary"]["from"] is None:
                        dict_vacancy.append(
                            {
                                "id": int(vacancy["id"]),
                                "name": vacancy["name"],
                                "salary": vacancy["salary"]["to"],
                                "requirement": vacancy["snippet"]["requirement"],
                                "url": vacancy["alternate_url"],
                            }
                        )

                    elif vacancy["salary"] and vacancy["salary"]["to"] is None:
                        dict_vacancy.append(
                            {
                                "id": int(vacancy["id"]),
                                "name": vacancy["name"],
                                "salary": vacancy["salary"]["from"],
                                "requirement": vacancy["snippet"]["requirement"],
                                "url": vacancy["alternate_url"],
                            }
                        )

            return dict_vacancy

        else:
            return "Возникла ошибка с подключением к API hh.ru"
