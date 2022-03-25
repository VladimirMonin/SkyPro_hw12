# Имортируем класс блюпринта
from flask import Blueprint, request
# Импортируем функции
from functions import load_posts_json, search_post

# Импортируем шаблонизатор
from flask import render_template

# Рожаем новый блюпринт, выбираем ему имя :)
# Добавляем настройку кастомной папки с шаблонами
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создаем вьюшку главной страницы (в декораторе блюпринт а не app!)
@main_blueprint.route('/')
def main():
    return render_template('index.html')


# Создаем вьюшку страницы поисковой выдачи (post_list.html)
@main_blueprint.route('/search/')
def search_page():
    search_str = request.args.get('s')
    posts_list = load_posts_json()
    find_posts = search_post(posts_list, search_str)
    post_count = len(posts_list)
    # Тут надо функцию поиска по json нужных постов
    return render_template('post_list.html', posts=find_posts, count=post_count, search_str=search_str)  # Наверное стоит сделать условие по длине списка? (Посты не найдены)
