from flask import Flask, Blueprint, request
from flask_login import login_required, current_user
from app.models import db, League, User, Player, UserTeam, UserTeamPlayer
from app.forms import UserTeamForm

user_team_routes = Blueprint("user_teams", __name__)


# Get Team By Id
@user_team_routes.route("/<int:id>")
@login_required
def get_team(id):
    team = UserTeam.query.get(id)
    return {"team": team.to_dict()}


# CREATE TEAM
@user_team_routes.route("/league/<int:league_id>", methods=["POST"])
@login_required
def create_team(league_id):
    userId = int(current_user.id)
    league = League.query.get(league_id)
    if (league == None):
        return {"errors": ["League does not exist"]}, 404
    res = request.get_json()
    print("RES ------->", res)
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


# Delete Team
@user_team_routes.route("/<user_team_id>", methods=["DELETE"])
@login_required
def delete_team(user_team_id):
    userId = int(current_user.id)

    team = UserTeam.query.get(user_team_id)
    if (team == None):
        return {"errors": ["Team does not exist"]}, 404



# Get Players of Team
@user_team_routes.route("/<int:id>/players")
def get_team_players(id):
    team = UserTeam.query.get(id)
    players = team.players
    return {"players": [player.to_dict() for player in players]}








# ADD Player to Team
@user_team_routes.route("/<int:user_team_id>/player/<int:player_id>", methods=["POST"])
@login_required
def add_player(user_team_id, player_id):
    team = UserTeam.query.get(user_team_id)
    if (team == None):
        return {"errors": ["Team does not exist"]}, 404

    player = Player.query.get(player_id)
    if (player == None):
        return {"errors": ["Player does not exist"]}, 404
    
    new_team_player = UserTeamPlayer(
        user_team_id=user_team_id,
        player_id=player_id
    )

    return {"newPlayer": player.to_dict()}


# DELETE Player from Team
@user_team_routes.route("/<int:user_team_id>/player/<int:player_id>", methods=["DELETE"])
@login_required
def remove_player(user_team_id, player_id):
    team = UserTeam.query.get(user_team_id)
    if (team == None):
        return {"errors": ["Team does not exist"]}, 404

    player = Player.query.get(player_id)
    if (player == None):
        return {"errors": ["Player does not exist"]}, 404

    user_team_player = UserTeamPlayer.query.filter(UserTeamPlayer.user_team_id == user_team_id, UserTeamPlayer.player_id == player_id).all()
    if (len(user_team_player) == 0):
        return {"errors": ["Player is not in this team"]}, 404

    db.session.delete(user_team_player),
    db.session.commit()

    return {"removedPlayer": player.to_dict()}
