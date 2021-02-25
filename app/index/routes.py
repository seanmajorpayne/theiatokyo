from flask import render_template
from app.google import google_api

from app.index import bp


@bp.route("/")
@bp.route("/index")
def index():
    views = 1
    subscribers = 2
    return render_template(
        "/index.html", variable=views, variable2=subscribers, year="2020"
    )
