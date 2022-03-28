from flask import Flask, request, render_template, send_from_directory

from main.main_views import main_blueprint
from loader.loader_views import loader_blueprint

from constant import *

app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(main_blueprint, url_prefix="/")
app.register_blueprint(loader_blueprint)


# Разрешаем доступ к картинкам (показ после загрузки)
@app.route(f'/post/loaded/<path:path>/')
def img_dir(path):
    return send_from_directory(IMAGES_FOLDER, path)  # СЛЕЕЕЕШ!!!!


# Разрешаем доступ к картинкам (показ картинок с диска в поле поиска и в ленте)
@app.route(f'/search/<path:path>/')
def img_dir2(path):
    return send_from_directory(IMAGES_FOLDER, path)


app.run(debug=True)
