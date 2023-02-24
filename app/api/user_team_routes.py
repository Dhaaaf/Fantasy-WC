from flask import Flask, Blueprint, request
from flask_login import login_required, current_user
from app.models import db, League, User, Player, UserTeam
from app.forms import UserTeamForm

user_team_routes = Blueprint("user_teams", __name__)


# Get Team By Id
@user_team_routes.route("/<int:id>")
@login_required
def get_team(id):
    team = UserTeam.query.get(id)
    return {"team": team.to_dict()}


# CREATE TEAM
@user_team_routes.route("/league/<int:league_id>/new")
@login_required
def create_team(league_id):
    userId = int(current_user.id)
    league = League.query.get(league_id)
    if (league == None):
        return {"errors": ["League does not exist"]}, 404
    res = request.get_json()
    form = UserTeamForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        team = UserTeam(
            user_id=userId,
            name=res["name"],
            points=0,
            league_id=league_id,
            bank=league.team_budget,
            match_day=0
        )
        db.session.add(team)
        db.session.commit()
    
    return {"team": team.to_dict()}, 201
