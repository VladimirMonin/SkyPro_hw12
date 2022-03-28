# Имортируем класс блюпринта
from flask import Blueprint, request
# Импортируем константы
from constant import *

# Импортируем шаблонизатор
from flask import render_template

# Импортируем функции
from functions import load_posts_json, dump_posts_json

# Рожаем новый блюпринт, выбираем ему имя :)
# Добавляем настройку кастомной папки с шаблонами
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', url_prefix='/post/')


# Создаем вьюшку тестовую страницы (в декораторе блюпринт а не app!)
@loader_blueprint.route('/form/')
def main():
    return render_template('post_form.html')


@loader_blueprint.route('/loaded/', methods=['POST'])
def get_load_form():
    # Получаем текст поста из формы
    post_text = request.form['content']

    # Получаем объект картинки из формы
    picture = request.files.get("picture")

    # Получаем имя файла у загруженного фала
    filename = picture.filename

    # Сохраняем картинку под родным именем в папку uploads
    full_picture_path = f"{IMAGES_FOLDER}{filename}"
    picture.save(full_picture_path)
    dump_posts_json(filename, post_text)
    return render_template('post_uploaded.html', picture=f'/post/loaded/{filename}', post_text=post_text)
