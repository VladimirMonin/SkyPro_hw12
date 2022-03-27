# Имортируем класс блюпринта
from flask import Blueprint, request
# Импортируем функции ?

# Импортируем шаблонизатор
from flask import render_template

# Рожаем новый блюпринт, выбираем ему имя :)
# Добавляем настройку кастомной папки с шаблонами
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


# Создаем вьюшку тестовую страницы (в декораторе блюпринт а не app!)
@loader_blueprint.route('/loader/')
def main():
    return render_template('post_form.html')


@loader_blueprint.route('/loaded/', methods=['POST'])
def nmain():
    # Получаем текст поста из формы
    post_text = request.form['content']

    # Получаем объект картинки из формы
    picture = request.files.get("picture")

    # Получаем имя файла у загруженного фала
    filename = picture.filename

    # Сохраняем картинку под родным именем в папку uploads
    picture.save(f"./static/uploads/images/{filename}")
    return render_template('post_uploaded.html', picture=filename, post_text=post_text)
