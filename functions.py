import json
from constant import *

#
def load_posts_json(filename=JSON_FILE):
    """
    Функция читает json с вопросами и возвращает словарь для игры
    :param filename: По умолчанию questions.json
    :return: Словарь
    """
    try:
        file = open(filename, encoding='UTF-8')
        candidates = json.load(file)
        file.close()
        return candidates
    except ValueError:
        return 'Ошибка чтения файла'
    except FileNotFoundError:
        return 'Ошибка. Файл json не найден'



# ВОПРОС. В КАКОМ ВАРИАНТЕ ПРАВИЛЬНО ЭТО ДЕЛАТЬ? Выдавать во вьюшку готовый результат, или весь список,
# а поиск делать циклом в HTML? В ЛЮБОМ ли варианте обработка будет на сервере? Или если отдать в HTML - весь json
# пойдет в браузер юзера и там будет перебор циклом? Это безопасно?

def search_post(posts_list, search_post):
    """Функция принимает список постов и производит поиск по вхождению строки"""
    result_list = []
    for post in posts_list:
        if search_post.lower() in post['content'].lower():
            if 'http' not in post['pic']:  # ЕСЛИ в строке нет http то мы уже отдаем не ссылку, а адрес по которому есть доступ к файлам на диске
                post['pic'] = '/search/' + post['pic'].split('/')[-1]
            result_list.append(post)
    return result_list


def dump_posts_json(picture_name, content, picture_path=IMAGES_FOLDER):
    """
    Функция записи в json. Принимает название картинки и пост. Путь к папке задан константой)
    :param picture_name: Имя картинки
    :param content: Текст поста
    :param picture_path: Путь к папке с медиа. Константа
    :return:
    """
    file = load_posts_json()
    for_append = {"pic": picture_path + picture_name, "content": content}
    file.append(for_append)
    try:
        with open(JSON_FILE, 'w', encoding='UTF-8') as f:
            json.dump(file, f, indent=4, ensure_ascii=False)
    except ValueError:
        return 'Ошибка чтения файла'
    except FileNotFoundError:
        return 'Ошибка. Файл json не найден'