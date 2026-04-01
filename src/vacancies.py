class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("id", "name", "salary", "requirement", "url")

    def __validate_id(self, id: int) -> int or str:
        """Метод валидации ID вакансии"""

        if not isinstance(id, int):
            return "Отсутсвует"
        return id

    def __validate_name(self, name: str) -> str:
        """Метод валидации имени вакансии"""

        if not isinstance(name, str) or not name or name.split() == []:
            return "Отсутствует"
        return name

    def __validate_salary(self, salary: int) -> int:
        """Метод валидации зарплаты"""

        if not isinstance(salary, int) or salary <= 0:
            return 0
        return salary

    def __validate_requirement(self, requirement: str) -> str:
        """Метод валидации требований вакансии"""

        if not isinstance(requirement, str) or not requirement or requirement.split() == []:
            return "Не указаны"
        return requirement

    def __validate_url(self, url: str) -> str:
        """Метод валидации ссылки на вакансию"""

        if not isinstance(url, str) or not url:
            return "Ссылка на вакансию отсутствует"
        return url

    def __init__(self, id, name, salary, requirement, url):
        self.id = self.__validate_id(id)
        self.name = self.__validate_name(name)
        self.salary = self.__validate_salary(salary)
        self.requirement = self.__validate_requirement(requirement)
        self.url = self.__validate_url(url)

    def __lt__(self, other):
        return self < other

    def __le__(self, other):
        return self <= other

    def __gt__(self, other):
        return self > other

    def __ge__(self, other):
        return self >= other

    def __repr__(self):
        return (
            f"Vacancy(ID='{self.id}, name='{self.name}', salary='{self.salary}', requirement='{self.requirement}',"
            f" url='{self.url}')"
        )

    def to_dict(self) -> dict:
        """Метод собирающий данные введеные пользователем в словарь"""

        return {
            "id": self.id,
            "name": self.name,
            "salary": self.salary,
            "requirement": self.requirement,
            "url": self.url,
        }
