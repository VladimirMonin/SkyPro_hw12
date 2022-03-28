# Имортируем класс блюпринта
from flask import Blueprint, request
# Импортируем функции
from functions import load_posts_json, search_post
# Импортируем логирование
import logging

# Включаем логирование
logging.basicConfig(encoding='utf-8', level=logging.INFO)
# Импортируем шаблонизатор
from flask import render_template

# Рожаем новый блюпринт, выбираем ему имя :)
# Добавляем настройку кастомной папки с шаблонами
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создаем вьюшку главной страницы (в декораторе блюпринт а не app!)
@main_blueprint.route('/')
def main():
    return render_template(
        'index.html')  # ВОПРОС. Почему у нас в домашке на главной странице вместо ленты постов форма ПОИСКА???!


# Создаем вьюшку страницы поисковой выдачи (post_list.html)
@main_blueprint.route('/search/')
def search_page():
    search_str = request.args.get('s')  # Получаем поисковый запрос из урла
    logging.info(f'Поисковая фраза: {search_str}')
    posts_list = load_posts_json()  # Загружаем список постов из файла. Сделал тут, т.к. посты ведь будут появлятся новые. Чтобы данные были сввежими
    find_posts = search_post(posts_list, search_str)  # Производим поиск поста
    post_count = len(posts_list)  # Длина списка (для доп. фитч)
    return render_template('post_list.html', posts=find_posts, count=post_count,
                           search_str=search_str)  # Наверное стоит сделать условие по длине списка? (Посты не найдены)
