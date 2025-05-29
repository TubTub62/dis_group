from flask import render_template
from steamStats import app
from flask import Blueprint

stats = Blueprint('stats', __name__)

@stats.route("/")
@stats.route("/index")
def index():
    return render_template("base.html")

@app.errorhandler(404)
def not_found():
    print("WTF")