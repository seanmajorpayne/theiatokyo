from flask import render_template
from app.nito.nito import Eyexplore

from app.nito import bp

NITO = Nito()


@bp.route("/pullstay")
def eyexplore_case():
    views = Nito.get_views()
    subscribers = Nito.get_subscribers()
    return render_template(
        "nito/pullstay.html",
        views=views,
        subscribers=subscribers,
        year=2021,
    )