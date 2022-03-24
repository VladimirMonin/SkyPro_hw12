#Имортируем класс блюпринта
from flask import Blueprint

#Рожаем новый блюпринт, выбираем ему имя :)
main_blueprint = Blueprint('main_blueprint', __name__)

#Создаем вьюшку (в декораторе блюпринт а не app!)
@main_blueprint.route('/')
def main():
    return 'Это блюпринт, детка!'