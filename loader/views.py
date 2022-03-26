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

@loader_blueprint.route('/loaded/')
def nmain():
    picture = request.files.get('picture').filename
    return render_template('post_uploadad.html', picture=picture)