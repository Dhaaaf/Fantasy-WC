from .db import db, environment, SCHEMA, add_prefix_for_prod

class UserTeamPlayer(db.Model):
    __tablename__ = "user_teams_players_table"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_team_id = db.Column(db.Integer, db.ForeignKey('user_teams_table.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players_table.id'), nullable=False)
