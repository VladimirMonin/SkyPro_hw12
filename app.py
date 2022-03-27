from flask import Flask, request, render_template, send_from_directory

from main.main_views import main_blueprint
from loader.loader_views import loader_blueprint

from constant import *

app = Flask(__name__)

app.register_blueprint(main_blueprint, url_prefix="/")
app.register_blueprint(loader_blueprint)


@app.route(f'/post/loaded/<path:path>/')
def img_dir(path):
    return send_from_directory('uploads/images/', path)  # СЛЕЕЕЕШ!!!!


app.run(debug=True)
