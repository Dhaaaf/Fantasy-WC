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


# NEXT MATCHDAY
@user_team_routes.route("/<user_team_id>/next_match", methods=["PUT"])
@login_required
def next_match(user_team_id):
    team_id = user_team_id
    userId = int(current_user.id)
    team = UserTeam.query.get(user_team_id)
    if (team == None):
        return {"errors": ["Team does not exist"]}, 404

    if(team.user_id != userId):
        return {"errors": ["This team doesn't belong to this user"]}, 403

    res = request.get_json()
    # print("RES------->",res)
    # print("RES transfers------->",res["transfersLeft"])
    # print("RES playerIds------->",res["teamPlayersIds"])
    # print("RES playerIds------->",res["bank"])


    #GET ALL CURRENT PLAYERS AND DELETE



    user_team_players = UserTeamPlayer.query.filter_by(user_team_id=team_id).all()
    for user_team_player in user_team_players:
        db.session.delete(user_team_player)
        db.session.commit()



    #LOOP OVER ARRAY OF NEW PLAYERS AND ADD TO INSTANCE

    for id in res["teamPlayersIds"]:
        new_team_player = UserTeamPlayer(
            user_team_id=team_id,
            player_id=id
            )
        db.session.add(new_team_player)
        db.session.commit()


    

    # NEW BANK

    team.bank = res["bank"]
    team.match_day = team.match_day + 1
    db.session.commit()

    # ADD POINTS

    new_players = team.players
    # print("ALL NEW PLAYERS ---->", new_players)
    add_points = 0
    for player in team.players:
        add_points += player.game_week_stats[team.match_day - 1].points

    team.points += add_points
    db.session.commit()

    # CHECK FOR EXTRA TRANSFERS
    if res["transfersLeft"] < 0:
        subtract_points = res["transfersLeft"] * 4
        team.points += subtract_points
        db.session.commit()

    return {"team": team.to_dict()}, 201


# Edit Team Name
@user_team_routes.route("/<user_team_id>", methods=["PUT"])
@login_required
def edit_team_name(user_team_id):
    userId = int(current_user.id)
    res = request.get_json()

    team = UserTeam.query.get(user_team_id)
    if (team == None):
        return {"errors": ["Team does not exist"]}, 404

    if(team.user_id != userId):
        return {"errors": ["This team doesn't belong to this user"]}, 403

    team.name = res["name"]
    db.session.commit()

    return {"team": team}


# Delete Team
@user_team_routes.route("/<user_team_id>", methods=["DELETE"])
@login_required
def delete_team(user_team_id):
    userId = int(current_user.id)

    team = UserTeam.query.get(user_team_id)
    if (team == None):
        return {"errors": ["Team does not exist"]}, 404

    if(team.user_id != userId):
        return {"errors": ["This team doesn't belong to this user"]}, 403

    db.session.delete(team)
    db.session.commit()
    return {"team": user_team_id}



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
