from flask import Blueprint

bp = Blueprint("nito", __name__)

from app.nito import routes
