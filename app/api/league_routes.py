from flask import Flask, Blueprint, request
from flask_login import login_required, current_user
from app.models import db, League, User, LeaguesTournament
from app.forms import LeagueFrom

#  url_prefix="/api/leagues
league_routes = Blueprint("leagues", __name__)


# GET ALL LEAGUES
@league_routes.route("/")
@login_required
def leagues():
    leagues = League.query.all()
    return {"leagues": [league.to_dict() for league in leagues]}, 201

# GET USER'S LEAGUES
@league_routes.route("/user")
@login_required
def leagues_user():
    leagues = current_user.leagues
    return {"leagues": [league.to_dict() for league in leagues]}, 201

# GET LEAGUES WHICH ARE PUBLIC AND USER'S
@league_routes.route("/public")
@login_required
def leagues_public():
    league1 = League.query.filter_by(is_private=False).all()
    user_leagues = current_user.leagues
    leagues = list(set(league1).union(set(user_leagues)))
    return {"leagues": [league.to_dict() for league in leagues]}, 201


# CREATE LEAGUE
@league_routes.route("/new", methods=["POST"])
@login_required
def create_league():
    userId = int(current_user.id)
    res = request.get_json()
    form = LeagueFrom()
    form["csrf_token"].data = request.cookies["csrf_token"]
    tournaments = res["tournaments"]
    if tournaments == None:
        return {"error": ["League must choose atleast one tournament"]}, 403


    if len(tournaments) < 1:
        return {"error": ["League must choose atleast one tournament"]}, 403

    if form.validate_on_submit():
        league = League (
            owner_id=userId,
            name=res["name"],
            display_pic=res["display_pic"],
            team_budget=res["team_budget"],
            is_private=res["is_private"],
        )
        db.session.add(league)
        db.session.commit()
        for tournament in tournaments:
            league_tournament = LeaguesTournament(
                league_id=league.id,
                tournament_id=tournament
            )
            db.session.add(league_tournament)
            db.session.commit()
        
        return {"league": league.to_dict()}, 201



# EDIT LEAGUE
@league_routes.route("/<int:id>", methods=["PUT"])
@login_required
def edit_league(id):
    userId = int(current_user.id)
    league = League.query.get(id)
    if (league == None):
        return {"errors": ["League does not exist"]}, 404
    if (league.owner_id != userId):
        return {"errors": ["This league doesn't belong to this user"]}, 403
    
    res = request.get_json()
    form = LeagueFrom()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        league.name = res["name"]
        league.display_pic = res["display_pic"]
        league.is_private = res["is_private"]
        return {"league": league.to_dict()}, 200
    
    return form.errors


# DELETE LEAGUE
@league_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_league(id):
    userId = int(current_user.id)
    league = League.query.get(id)
    if (league == None):
        return {"errors": ["League does not exist"]}, 404
    if (league.owner_id != userId):
        return {"errors": ["This league doesn't belong to this user"]}, 403

    db.session.delete(league)
    db.session.commit()

    return {"league": id}
