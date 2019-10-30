"""


"""

__author__ = "Li Wei (liw@sicnu.edu.cn)"


from flask import Flask
from flask import Blueprint

app = Flask(__name__)
bp = Blueprint("bp", __name__)


@bp.route("/index")     # http://127.0.0.1:5000/index
def index():
    return "Hello Blueprint"


app.register_blueprint(bp)


if __name__ == "__main__":
    print(app.view_functions)
    print(app.url_map)
    app.run()
