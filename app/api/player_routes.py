from flask import Flask, Blueprint, request
from flask_login import login_required, current_user
from app.models import db, League, User, Player, UserTeam

player_routes = Blueprint("players", __name__)

# Get Players by League
@player_routes.route("/league/<int:leagueId>")
@login_required
def get_players(leagueId):
    league = League.query.get(leagueId)
    if (league == None):
        return {"errors": ["League does not exist"]}, 404
    tournaments = league.tournaments
    all_players = [player for tournament in tournaments for player in tournament.players]
    return {"players": [player.to_dict() for player in all_players]}
