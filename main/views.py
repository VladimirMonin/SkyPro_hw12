# Имортируем класс блюпринта
from flask import Blueprint

# Импортируем шаблонизатор
from flask import render_template

# Рожаем новый блюпринт, выбираем ему имя :)
# Добавляем настройку кастомной папки с шаблонами
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Создаем вьюшку главной страницы (в декораторе блюпринт а не app!)
@main_blueprint.route('/')
def main():
    return render_template('index.html')

# С