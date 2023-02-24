from flask import Flask, Blueprint, request
from flask_login import login_required, current_user
from app.models import Tournament

tournament_routes = Blueprint("tournaments", __name__)

#GET ALL TOURNAMENTS

@tournament_routes.route("/")
@login_required
def tournaments():
    tournaments = Tournament.query.all()
    return {"tournaments": [tournament.to_dict() for tournament in tournaments]}
