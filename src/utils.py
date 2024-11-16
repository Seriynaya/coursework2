def top_vacancies(number, my_list):
    """Функция вывода Топ-n вакансий"""
    try:
        n = int(number)
        return my_list[:n] if n > 0 else my_list
    except ValueError:
        return my_list


def filter_vacancies(my_list, words_list):
    """Функция фильтрации вакансий по ключевым словам"""
    filtered_vacancies = []
    for index in my_list:
        for info in words_list:
            if index["description"] is None:
                continue
            elif info in index["description"] or info in index["name"]:
                filtered_vacancies.append(index)
    return filtered_vacancies
