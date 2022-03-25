import json


def load_post_json(filename='posts.json'):
    """
    Функция читает json с вопросами и возвращает словарь для игры
    :param filename: По умолчанию questions.json
    :return: Словарь
    """
    file = open(filename, encoding='UTF-8')
    candidates = json.load(file)
    file.close()
    return candidates


def search_post(posts_list, search_post):
    """Функция принимает список постов и производит поиск по вхождению строки"""
    pass
