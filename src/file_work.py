import json
from abc import ABC, abstractmethod
from json import JSONDecodeError


class FileWork(ABC):
    """Абстрактный класс для работы с файлами"""

    def __init__(self, filename):
        self._filename = filename

    @abstractmethod
    def add_vacancy(self, vacancy: dict) -> json.dump:
        pass

    @abstractmethod
    def get_data_from_file(self) -> list:
        pass

    @abstractmethod
    def file_cleaning(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancies_list: list) -> json.dump:
        pass


class WorkingWithJSON(FileWork):
    """Класс отвечающий за взаимодействие с файлом 'vacancies.json'"""

    data = list

    def __init__(self, filename="vacancies.json"):
        super().__init__(filename)
        self.data = []

    def add_vacancy(self, vacancy) -> json.dump:
        """Добавление вакансий в файл 'vacancies.json'"""

        self.get_data_from_file()
        self.data.append(vacancy)

        with open(self._filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False)

    def get_data_from_file(self) -> list:
        """Получение вакансий из файла 'vacancies.json', если файла не существует то создает его"""

        try:
            with open(self._filename, "r", encoding="utf-8") as f:
                self.data = json.load(f)
                return self.data

        except JSONDecodeError:
            self.data = []

        except FileNotFoundError:
            with open(self._filename, "w", encoding="utf-8"):
                status = "Файл создан"

    def file_cleaning(self):
        """Очищает файл 'vacancies.json'"""

        with open(self._filename, "w", encoding="utf-8") as f:
            del f

    def delete_vacancy(self, vacancies_list) -> json.dump:
        """Удаляет вакансии выбраные пользователем из файла 'vacancies.json'"""

        data_file = self.get_data_from_file()
        clean_data_file = []

        for vacancy in data_file:
            if vacancy not in vacancies_list:
                clean_data_file.append(vacancy)

        self.file_cleaning()

        with open(self._filename, "w", encoding="utf-8") as f:
            json.dump(clean_data_file, f, ensure_ascii=False)
