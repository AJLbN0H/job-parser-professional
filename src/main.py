from src.api import HeadHunterAPI
from src.file_work import WorkingWithJSON
from src.utils import (deleted_option, display_of_number_vacancies, display_of_vacancies, display_range_vacancies,
                       display_top_vacancies)
from src.vacancies import Vacancy

api_vacancies = HeadHunterAPI()
file_work = WorkingWithJSON()
vacant = Vacancy


def user_interaction():
    """Взаимодействие с пользователем"""

    while True:
        action_number = input(
            "\nВыберите номер действия:\n"
            "1. Поиск вакансий по ключевому слову\n"
            "2. Поиск вакансий в файле по ключевому слову или по ID\n"
            "3. Получить топ N вакансий по зарплате из файла\n"
            "4. Записать вакансию в файл\n"
            "5. Очистить файл с вакансиями\n"
            "6. Выход\n"
            "Выбран номер: "
        )

        if action_number == "1":
            status = 0
            while True:
                if status != 1:
                    user_selection = input(
                        "\nВыберете номер действия:"
                        "\n1. Начать поиск вакансий по ключевому слову"
                        "\n2. Назад"
                        "\nВыбран номер: "
                    )

                    if user_selection == "1":
                        while True:
                            if status != 1:
                                search_query = input("\nВведите поисковой запрос: ")

                                if not search_query.split():
                                    print("\nВы не ввели поисковой запрос!")

                                else:
                                    while True:
                                        if status != 1:
                                            try:
                                                top_vacancies = int(
                                                    input("\nВведите какое количество вакансий вы хотите получить: ")
                                                )
                                            except ValueError:
                                                print("\nВы неверно ввели количество вакансий!")
                                            else:

                                                if top_vacancies > 100:
                                                    print("\nБольше 100 вакансий получить нельзя!")

                                                elif 1 <= top_vacancies <= 100:
                                                    vacancies = api_vacancies.get_vacancies(
                                                        search_query, top_vacancies
                                                    )
                                                    if vacancies:
                                                        display_of_number_vacancies(len(vacancies), vacancies)
                                                        display_range_vacancies(top_vacancies, vacancies)

                                                        while True:
                                                            if status != 1:

                                                                save_option = input(
                                                                    "\nВыберете номер действия:"
                                                                    "\n1. Записать в файл"
                                                                    "\n2. Не записывать"
                                                                    "\nВыбран номер: "
                                                                )

                                                                if save_option == "1":
                                                                    for vacancy in vacancies:
                                                                        file_work.add_vacancy(vacancy)

                                                                    print(
                                                                        "\nВакансии сохранены в файл "
                                                                        "'vacancies.json'"
                                                                    )

                                                                    status = 1
                                                                    break

                                                                elif save_option == "2":

                                                                    status = 1
                                                                    break

                                                                else:
                                                                    print("\nВы ввели неверный номер действия!")

                                                    else:
                                                        print(f"\nВакансии по запросу '{search_query}' не найдены")

                                                        status = 1
                                                        break
                                                else:
                                                    print("\n0 вакансий получить нельзя!")
                                        else:
                                            break
                            else:
                                break

                    elif user_selection == "2":
                        break

                    else:
                        print("\nВы ввели неверный номер действия!")
                else:
                    break

        elif action_number == "2":
            status = 0
            while True:
                if status != 1:
                    data_vacancies = file_work.get_data_from_file()

                    if data_vacancies:
                        search_query = input(
                            "\nВыберите номер действия:"
                            "\n1. Поиск по ID"
                            "\n2. Поиск по ключевому слову"
                            "\n3. Назад"
                            "\nВыбран номер: "
                        )

                        if search_query == "1":
                            while True:
                                if status != 1:
                                    user_id = input("\nВведите ID вакансии: ")

                                    if len(user_id) == 9:
                                        try:
                                            int_user_id = int(user_id)
                                        except ValueError:
                                            print("\nВы неверно ввели ID!" "\nID состоит из 9 цифр")
                                        else:
                                            id_vacancies = []
                                            for vacancy in data_vacancies:
                                                if vacancy["id"] == int_user_id:
                                                    id_vacancies.append(vacancy)

                                            if id_vacancies:
                                                display_of_number_vacancies(len(id_vacancies), id_vacancies)
                                                display_of_vacancies(id_vacancies)
                                                deleted_option(id_vacancies)

                                                status = 1

                                            else:
                                                print(f"\nВакансии с ID: '{user_id}' не найдены")

                                                status = 1
                                                break

                                    else:
                                        print("\nВы неверно ввели ID!" "\nID состоит из 9 цифр")

                                else:
                                    break

                        elif search_query == "2":
                            while True:
                                if status != 1:
                                    user_search = input("\nВведите поисковой запрос: ")

                                    if not user_search.split():
                                        print("\nВы не ввели поисковой запрос!")

                                    else:
                                        id_vacancies = []

                                        for vacancy in data_vacancies:

                                            if "/" in vacancy["name"]:
                                                for i in vacancy["name"].replace("/", " ").split():

                                                    if "-" in i:
                                                        for i_ in i.replace("-", " ").split():

                                                            if "(" in i_ or ")" in i_:
                                                                for i__ in i_.replace("(", " ").split():
                                                                    for i___ in i__.replace(")", " ").split():
                                                                        if user_search.lower() == i___.lower():
                                                                            id_vacancies.append(vacancy)

                                                            else:
                                                                if user_search.lower() == i_.lower():
                                                                    id_vacancies.append(vacancy)

                                                    elif "(" in vacancy["name"] or ")" in i:
                                                        for i_ in i.replace("(", " ").split():
                                                            for i__ in i_.replace(")", " ").split():
                                                                if user_search.lower() == i__.lower():
                                                                    id_vacancies.append(vacancy)

                                                    else:
                                                        if user_search.lower() == i.lower():
                                                            id_vacancies.append(vacancy)

                                            elif "-" in vacancy["name"]:
                                                for i in vacancy["name"].replace("-", " ").split():

                                                    if "/" in i:
                                                        for i_ in i.replace("/", " ").split():

                                                            if "(" in i_ or ")" in i_:
                                                                for i__ in i_.replace("(", " ").split():
                                                                    for i___ in i__.replace(")", " ").split():
                                                                        if user_search.lower() == i___.lower():
                                                                            id_vacancies.append(vacancy)

                                                            else:
                                                                if user_search.lower() == i_.lower():
                                                                    id_vacancies.append(vacancy)

                                                    elif "(" in vacancy["name"] or ")" in i:
                                                        for i_ in i.replace("(", " ").split():
                                                            for i__ in i_.replace(")", " ").split():
                                                                if user_search.lower() == i__.lower():
                                                                    id_vacancies.append(vacancy)

                                                    else:
                                                        if user_search.lower() == i.lower():
                                                            id_vacancies.append(vacancy)

                                            elif "(" in vacancy["name"] or ")" in vacancy["name"]:
                                                for i in vacancy["name"].replace("(", " ").split():
                                                    for i_ in i.replace(")", " ").split():

                                                        if "/" in i_:
                                                            for i__ in i_.replace("/", " ").split():

                                                                if "-" in i__:
                                                                    for i___ in i__.replace("-", " ").split():
                                                                        if user_search.lower() == i___.lower():
                                                                            id_vacancies.append(vacancy)

                                                                else:
                                                                    if user_search.lower() == i__.lower():
                                                                        id_vacancies.append(vacancy)

                                                        elif "-" in i_:
                                                            for i__ in i_.replace("-", " ").split():
                                                                if user_search.lower() == i__.lower():
                                                                    id_vacancies.append(vacancy)

                                                        else:
                                                            if user_search.lower() == i_.lower():
                                                                id_vacancies.append(vacancy)

                                            else:
                                                if user_search.lower() == vacancy["name"].lower():
                                                    id_vacancies.append(vacancy)

                                        if id_vacancies:
                                            display_of_number_vacancies(len(id_vacancies), id_vacancies)
                                            display_of_vacancies(id_vacancies)
                                            deleted_option(id_vacancies)

                                            status = 1

                                        else:
                                            print(f"\nВакансии с названием: '{user_search}' не найдены")

                                            status = 1
                                            break

                                else:
                                    break

                        elif search_query == "3":
                            break

                        else:
                            print("\nВы ввели неверный номер действия!")

                    else:
                        print("\nФайл 'vacancies.json' пуст")
                        status = 1
                        break

                else:
                    break

        elif action_number == "3":
            status = 0
            while True:
                if status != 1:
                    data_vacancies = file_work.get_data_from_file()

                    if data_vacancies:
                        user_selection_1 = input(
                            "\nВыберете номер действия:"
                            "\n1. Получить топ N вакансий по зарплате из файла 'vacancies.json'"
                            "\n2. Назад"
                            "\nВыбран номер: "
                        )

                        if user_selection_1 == "1":
                            while True:
                                if status != 1:

                                    user_selection_2 = input(
                                        "\nВыберете номер действия:"
                                        "\n1. Указать диапазон зарплат"
                                        "\n2. Не указывать"
                                        "\n3. Назад"
                                        "\nВыбран номер: "
                                    )

                                    if user_selection_2 == "1":
                                        while True:
                                            if status != 1:
                                                salary = []
                                                for vacancy in data_vacancies:
                                                    salary.append(vacancy["salary"])

                                                try:
                                                    print(
                                                        f"\nВведите диапазон зарплат"
                                                        f"(От: '{min(salary)}' - До: '{max(salary)}'):"
                                                    )
                                                    from_ = int(input("От: "))
                                                except ValueError:
                                                    print("\nВы неверно ввели диапазон зарплат!")
                                                else:
                                                    while True:
                                                        if status != 1:
                                                            try:
                                                                print(
                                                                    f"\nВведите диапазон зарплат"
                                                                    f"(От: '{min(salary)}' - До: '{max(salary)}'):"
                                                                )
                                                                to_ = int(input("До: "))
                                                            except ValueError:
                                                                print("\nВы неверно ввели диапазон зарплат!")
                                                            else:
                                                                range_vacancies = []
                                                                for vacancy in data_vacancies:
                                                                    if from_ <= vacancy["salary"] <= to_:
                                                                        range_vacancies.append(vacancy)

                                                                display_of_number_vacancies(
                                                                    len(range_vacancies), range_vacancies
                                                                )
                                                                if range_vacancies:
                                                                    display_top_vacancies(range_vacancies)
                                                                    status = 1
                                                                    break

                                                                else:
                                                                    status = 1
                                                                    break

                                            else:
                                                break

                                    elif user_selection_2 == "2":
                                        display_of_number_vacancies(len(data_vacancies), data_vacancies)
                                        display_top_vacancies(data_vacancies)

                                        status = 1
                                        break

                                    elif user_selection_2 == "3":
                                        break

                                    else:
                                        print("\nВы ввели неверный номер действия!")

                                else:
                                    break

                        elif user_selection_1 == "2":
                            break

                        else:
                            print("\nВы ввели неверный номер действия!")

                    else:
                        print("\nФайл 'vacancies.json' пуст")
                        break

                else:
                    break

        elif action_number == "4":
            status = 0
            while True:
                if status != 1:
                    user_selection = input(
                        "\nВыберете номер действия:"
                        "\n1. Начать запись вакансии в файл"
                        "\n2. Назад"
                        "\nВыбран номер: "
                    )

                    if user_selection == "1":
                        while True:
                            if status != 1:
                                id = input("\nID: ")

                                if len(id) == 9:
                                    try:
                                        int_id = int(id)
                                    except ValueError:
                                        print("\nВы неверно ввели ID!" "\nID состоит из 9 цифр")
                                    else:
                                        name = input("Название: ")

                                        while True:
                                            if status != 1:
                                                try:
                                                    salary = int(input("Зарплата: "))
                                                except ValueError:
                                                    print("Неверно введена зарплата!")
                                                else:
                                                    requirement = input("Требования: ")

                                                    url = f"https://hh.ru/vacancy/{int_id}"

                                                    vacancy = Vacancy(
                                                        id=int_id,
                                                        name=name,
                                                        salary=salary,
                                                        requirement=requirement,
                                                        url=url,
                                                    )
                                                    file_work.add_vacancy(vacancy.to_dict())

                                                    print("\nВакансия:")
                                                    display_of_vacancies([vacancy.to_dict()])
                                                    print("\nЗаписана в файл 'vacancies.json'")

                                                    status = 1
                                                    break

                                            else:
                                                break

                                else:
                                    print("\nВы неверно ввели ID!" "\nID состоит из 9 цифр")

                            else:
                                break

                    elif user_selection == "2":
                        break

                    else:
                        print("\nВы ввели неверный номер действия!")

                else:
                    break

        elif action_number == "5":
            file_work.file_cleaning()
            print("\nФайл 'vacancies.json' очищен")

        elif action_number == "6":
            break

        else:
            print("\nВы ввели неверный номер действия!")


if __name__ == "__main__":
    user_interaction()
