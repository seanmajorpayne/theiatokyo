from flask import Blueprint

bp = Blueprint("eyexplore", __name__)

from app.eyexplore import routes