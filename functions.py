import json


def load_posts_json(filename='posts.json'):
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
# ВОПРОС. В КАКОМ ВАРИАНТЕ ПРАВИЛЬНО ЭТО ДЕЛАТЬ? Выдавать во вьюшку готовый результат, или весь список, а поиск делать циклом в HTML?
# В ЛЮБОМ ли варианте обработка будет на сервере? Или если отдать в HTML - весь json пойдет в браузер юзера и там будет перебор циклом? Это безопасно?
    """Функция принимает список постов и производит поиск по вхождению строки"""
    result_list = []
    for post in posts_list:
        if search_post.lower() in post['content'].lower():
            result_list.append(post)
    return result_list
